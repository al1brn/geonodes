#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 15:51:30 2023

@author: alain


simplify : Approximate a shape by a set of joining rectangles

"""

import numpy as np

DEBUG = False

BOT, RIGHT, TOP, LEFT = 0, 1, 2, 3

# ====================================================================================================
# Integer coordinates

class GPoint:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        
    def __str__(self):
        return f"<GPoint [{self.i:3d} {self.j:3d}]>"
        
    def __len__(self):
        return 2
    
    def __getitem__(self, index):
        if index == 0:
            return self.i
        elif index == 1:
            return self.j
        else:
            raise ValueError(f"Invalid index: {index}")
        
        return self.i if index == 0 else self.j
    
    def __setitem__(self, index, value):
        if hasattr(self,'__len__'):
            self.i = value[0]
            self.j = value[1]
        elif index == 0:
            self.i = value
        elif index == 1:
            self.j = value
        else:
            raise ValueError(f"Invalid index {index}")
            
    def __eq__(self, other):
        return self.i == other.i and self.j == other.j
            
    @property
    def to_int(self):
        return (self.j<<10) + self.i
    
    @classmethod
    def FromInt(cls, n):
        return cls(n & 0x3FF, n >> 10)
            
    def to_grid(self, grid, value):
        grid[self.i, self.j] = value
        
    def neighbour(self, direc):
        if direc == BOT:
            return GPoint(self.i,   self.j-1)
        elif direc == RIGHT:
            return GPoint(self.i+1, self.j  )
        elif direc == TOP:
            return GPoint(self.i,   self.j+1)
        elif direc == LEFT:
            return GPoint(self.i-1, self.j  )
        else:
            raise ValueError(f"Invalid direction {direc}")
            
    def left(self):
        return GPoint(self.i-1, self.j)
            
    def right(self):
        return GPoint(self.i+1, self.j)
            
    def bot(self):
        return GPoint(self.i, self.j-1)
            
    def top(self):
        return GPoint(self.i, self.j+1)
            

# ====================================================================================================
# Range of points

class PointRange:
    def __init__(self, p0, p1):
        
        self.p0 = p0
        self.p1 = p1
        
        di = p1.i - p0.i
        dj = p1.j - p0.j
        
        if di == 0 and dj == 0:
            self.counter = 0
            
        elif abs(di) > abs(dj):
            self.i_major = True
            self.counter = abs(di)
            self.mi = 1 if di > 0 else -1
            self.mj = dj/di
        else:
            self.i_major = False
            self.counter = abs(dj)
            self.mi = di/dj
            self.mj = 1 if dj > 0 else -1
            
    def __iter__(self):
        self.k = 0
        return self
    
    def __next__(self):
        if self.k < self.counter:
            k = self.k
            self.k += 1
            
            if self.i_major:
                return GPoint(self.p0.i + self.mi*k, self.p0.j + int(round(self.mj*k)))
            else:
                return GPoint(self.p0.i + int(round(self.mi*k)), self.p0.j + self.mj*k)

        else:
            raise StopIteration
            
# ====================================================================================================
# Grid rectangle
            
class GRect(list):
    
    def __init__(self, i0, j0, i1, j1):
        super().__init__()
        self.extend([i0, j0, i1, j1])
        self.check("Initialization")
        
    def __str__(self):
        return f"<GRect [{self.i0:3d} {self.j0:3d}] [{self.i1:3d} {self.j1:3d}], length: {self.length:3d} width: {self.width:3d}, surface: {self.surface}>"
        
    def check(self, title="Check", halt=False):
        if self.length <= 0 or self.width <= 0:
            if halt:
                raise Exception(f"{title}\nInvalid dimensions for a Grid Rectangle: length: {self.length}, width: {self.width}.")
            else:
                return False
        else:
            return True
        
    def clone(self):
        return GRect(*self)
    
    def verts(self, z=0.):
        return np.array(((self.i0, self.j0, z), (self.i1, self.j0, z), (self.i1, self.j1, z), (self.i0, self.j1, z)), float)
        
    @property
    def i0(self):
        return self[0]
    
    @i0.setter
    def i0(self, value):
        self[0] = value
        
    @property
    def j0(self):
        return self[1]
    
    @j0.setter
    def j0(self, value):
        self[1] = value
        
    @property
    def i1(self):
        return self[2]
    
    @i1.setter
    def i1(self, value):
        self[2] = value
        
    @property
    def j1(self):
        return self[3]
    
    @j1.setter
    def j1(self, value):
        self[3] = value
        
    @property
    def length(self):
        return self.i1 - self.i0
    
    @property
    def width(self):
        return self.j1 - self.j0
    
    @property
    def surface(self):
        return self.length*self.width
    
    def move_side(self, side_index, value):
        moved = self.clone()
        moved[side_index] += value
        if moved.check(halt=False):
            return moved
        else:
            return None
        
    @property
    def corners(self):
        return [GPoint(self.i0, self.j0), GPoint(self.i1, self.j0), GPoint(self.i1, self.j1), GPoint(self.i0, self.j1)]
    
    @property
    def inside_corners(self):
        return [GPoint(self.i0, self.j0), GPoint(self.i1-1, self.j0), GPoint(self.i1-1, self.j1-1), GPoint(self.i0, self.j1-1)]
    
    def contains(self, point):
        return point.i >= self.i0 and point.i < self.i1 and point.j >= self.j0 and point.j < self.j1
    
    @staticmethod
    def segment_intersect(a0, a1, b0, b1):
        if b0 < a0:
            # ......... a0 ......... a1 ......
            # .. b0
            if b1 <= a0:
                # ................ a0 ......... a1 ......
                # .. b0 .. b1
                return None, None
            
            if b1 < a1:
                # ......... a0 ......... a1 ....
                # .. b0 .......... b1 ..........
                return a0, b1
            
            else:
                # ......... a0 ......... a1 ....
                # .. b0 ..................... b1 ...
                return a0, a1
            
        elif b0 < a1:
            # .... a0 .................. a1 .....
            # .......... b0
            if b1 < a1:
                # ......... a0 .................. a1 .....
                # ............... b0 ...... b1 ...........
                return b0, b1
            else:
                # .... a0 ............. a1 ........
                # .......... b0 ............. b1 ..
                return b0, a1
            
        else:
            # ..... a0 ........ a1 ........
            # ....................... b0 ..
            return None, None
    
    def intersect(self, other):
        
        i0, i1 = self.segment_intersect(self.i0, self.i1, other.i0, other.i1)
        if i0 is None:
            return None

        j0, j1 = self.segment_intersect(self.j0, self.j1, other.j0, other.j1)
        if j0 is None:
            return None
        
        return GRect(i0, j0, i1, j1)
    
    def union(self, other):
        return GRect(min(self.i0, other.i0), min(self.j0, other.j0), max(self.i1, other.i1), max(self.j1, other.j1))
    
# ====================================================================================================
# A grid to shape the contours

class Grid:
    def __init__(self, shape):
        """ A grid of integer points.
        """
        self.a = np.zeros(shape, int)
        
    def __str__(self):
        return f"<Grid of shape {self.shape}>"
    
    @property
    def shape(self):
        return np.shape(self.a)
        
    @property
    def ni(self):
        return np.shape(self.a)[0]
        
    @property
    def nj(self):
        return np.shape(self.a)[1]
    
    def __len__(self):
        return len(self.a)
    
    def __getitem__(self, index):
        if isinstance(index, GPoint):
            return self.a[index.i, index.j]
        
        elif isinstance(index, GRect):
            return self.a[index.i0:index.i1, index.j0:index.j1]
        
        else:
            return self.a[index]
    
    def __setitem__(self, index, value):
        if isinstance(index, GPoint):
            self.a[index.i, index.j] = value
            
        elif isinstance(index, GRect):
            self.a[index.i0:index.i1, index.j0:index.j1] = value
            
        else:
            self.a[index] = value
    
    # ====================================================================================================
    # From another grid
    
    @classmethod
    def FromGrid(cls, grid):
        """ Initialize from another grid
        
        Args:
            - grid (Grid) : he grid to copy
        Returns:
            - Grid
        """
        g = cls(grid.shape)
        g.a[:] = self.a

        return g
    
    # ====================================================================================================
    # From verts
    
    @classmethod
    def FromVerts(cls, verts):
        
        origin = np.min(verts, axis=0)
        size   = np.max(verts, axis=0) - origin
        
        grid = cls((int(size[0]) + 5, int(size[1]) + 5))
        grid.origin = origin
        grid.size   = size
        
        rounded_verts = np.round(verts[:, :2] - origin[:2]).astype(int) + (2, 2)
        
        grid.draw_contour(rounded_verts, 1)
            
        if True and DEBUG:
            grid.plot("FromVerts", verts=verts)
            
        return grid
    
    def rects_to_verts(self, i_rects):
        
        rects = []
        for i_rect in i_rects:
            vs = i_rect - (2, 2, 0)
            vs += self.origin
            rects.append(vs)
            
        if True and DEBUG:
            for r in rects:
                self.plot("Rects from verts", verts=r)
            
            
        return rects
    
    # ====================================================================================================
    # Draw a segment
    
    def draw_segment(self, p0, p1, value, ok_slope=False):
        """ Draw a segment into the grid.
        
        Only horizontal and vertical lines are drawn to obtain rectangles.        
        """
        
        i0, j0, i1, j1 = p0.i, p0.j, p1.i, p1.j
        
        di = i1 - i0
        dj = j1 - j0
        
        # ----- Horizontal line
        
        if di == 0:
            if dj == 0:
                return
            
            if j0 < j1:
                self.a[i0, j0:j1+1] = value
            else:
                self.a[i0, j1:j0+1] = value
                
            return

        # ----- Vertical line
        
        if dj == 0:
            if i0 < i1:
                self.a[i0:i1+1, j0] = value
            else:
                self.a[i1:i0+1, j1] = value

            return
        
        # ----- General case

        mi = 1 if di > 0 else -1
        mj = 1 if dj > 0 else -1
        
        # Slope = 45°
        
        if ok_slope and abs(di) == abs(dj):
            for k in range(abs(di)+1):
                self.a[i0 + mi*k, j0 + mj*k] = value
            return
                
        # Another slope
        
        if ok_slope:
            if abs(di) > abs(dj):
                mj *= abs(dj/di)
                for k in range(abs(di)+1):
                    self.a[i0 + mi*k, j0 + int(round(mj*k))] = value
            else:
                mi *= abs(di/dj)
                for k in range(abs(dj)+1):
                    self.a[i0 + int(round(mi*k)), j0 + mj*k] = value
        else:
            if abs(di) > abs(dj):
                self.draw_segment(GPoint(i0, j0), GPoint(i1, j0), value)
                self.draw_segment(GPoint(i1, j0), GPoint(i1, j1), value)
            else:
                self.draw_segment(GPoint(i0, j0), GPoint(i0, j1), value)
                self.draw_segment(GPoint(i0, j1), GPoint(i1, j1), value)
                
    # ====================================================================================================
    # Draw a rectangle
    
    def draw_rect(self, rect, value):
        corners = rect.inside_corners
        for i in range(4):
            self.draw_segment(corners[i], corners[(i+1)%4], value)
            
    # ====================================================================================================
    # Draw an arbitrary shape
    # draw inside
    
    def draw_contour(self, coords, value, inside=True):
        
        def draw_hrz(i0, i1, j):
            if i1 > i0:
                self.a[i0:i1, j  ] = value
            else:
                self.a[i1:i0, j-1] = value
                
        def draw_vrt(j0, j1, i):
            if j1 > j0:
                self.a[i-1, j0:j1] = value
            else:
                self.a[i,   j1:j0] = value
        
        for i in range(len(coords)):
            
            A = coords[i]
            B = coords[(i+1)%len(coords)]
            
            di = B[0] - A[0]
            dj = B[1] - A[1]
            
            # ----- Horizontal segment
            
            if dj == 0:
                draw_hrz(A[0], B[0], B[1])
                    
            # ----- Vertical segment
                    
            elif di == 0:
                draw_vrt(A[1], B[1], A[0])
                    
            # ----- Slope en 2 segments
            
            elif np.sign(di)*np.sign(dj) > 0:
                draw_hrz(A[0], B[0], A[1])
                draw_vrt(A[1], B[1], B[0])
            else:
                draw_vrt(A[1], B[1], A[0])
                draw_hrz(A[0], B[0], B[1])
            
    
    # ====================================================================================================
    # Limits
    
    def contains(self, point):
        return point.i >= 0 and point.i < self.ni and point.j >= 0 and point.j < self.nj
    
    # ====================================================================================================
    # Neighbours of a cell matching a value
    # Neighbour indices are return as a int, see ij_to_int and int_to_ij
    
    def neighbours(self, point, value_is=None, value_is_not=None):
        """ The neighbours of a cell containing a given value.
        
        Args:
            - point (GPoint) : the pont
            - value (int) : grid value
        Returns:
            - np.ndarray of GPoints : the neighbours
        """
        
        nbs = []
        for direc in range(4):
            p = point.neighbour(direc)
            if self.contains(p):
                if value_is is not None:
                    if self[p] == value_is:
                        nbs.append(p)
                        
                elif value_is_not is not None:
                    if self[p] != value_is_not:
                        nbs.append(p)
                        
                else:
                    raise ValueError(f"Both ok_value and ko_value are None!")
        return nbs
    
    # ====================================================================================================
    # End point : continuing in a direction, give the last point:
    # - which has the cont_value if not None
    # - which has nont the stop_value if not None
    
    def end_point(self, point, direc, stop_value=None, cont_value=None):
        
        p = point
        for _ in range(max(self.ni, self.nj)):
            
            next_p = p.neighbour(direc)
            
            # Ret point
            ret = p if direc in [BOT, LEFT] else next_p 

            if not self.contains(next_p):
                return ret
            
            if stop_value is not None and self[next_p] == stop_value:
                return ret
            if cont_value is not None and self[next_p] != cont_value:
                return ret
            
            p = next_p
            
    def is_corner(self, point):
        if self[point] != 0:
            return False
        return len(self.neighbours(point, value_is_not=0)) >= 2
    
    def is_border(self, point):
        if self[point] != 0:
            return False
        return len(self.neighbours(point, value_is_not=0)) >= 1
    
    def get_corners(self):
        corners = []
        for i in range(1, self.ni-1):
            for j in range(1, self.nj-1):
                if self.is_corner(GPoint(i, j)):
                    corners.append(GPoint(i, j))
        return corners
    
    def rect_score(self, rect):
        assert(rect.surface > 0)
        return np.sum(self[rect] == 0), rect.surface
    
    def best_rect(self, rect0, rect1):
        
        if rect0 is None:
            return rect1
        if rect1 is None:
            return rect0
        
        f0, t0 = self.rect_score(rect0)
        f1, t1 = self.rect_score(rect1)
        r0, r1 = f0/t0, f1/t1
        
        if f0 == t0:
            if r1 > .95 and t1 > t0:
                return rect1
            else:
                return rect0
            
        elif f1 == t1:
            if r0 > .95 and t0 > t1:
                return rect0
            else:
                return rect1
            
        if r0 > r1:
            if r1 > .85 and t1 > t0:
                return rect1
            else:
                return rect0
        else:
            if r0 > .85 and t0 > t1:
                return rect0
            else:
                return rect1
        
            
    # ====================================================================================================
    # Fill the zone external to the border
    #
    # State of the grid: borders of been draw with 1 into a zero filled grid
    # After the fill: the exterior is filled with -1, the borders are erased to 0
    
    def fill_external(self):
        """ Fill the cells out of the house shape.
        """
        def fill_ext(point):
            if self[point] != 0:
                return
            
            cache = [point.to_int]
            while len(cache):
                for n in cache:
                    self[GPoint.FromInt(n)] = -1
                    
                new_cache = []
                for n in cache:
                    new_cache.extend([p.to_int for p in self.neighbours(GPoint.FromInt(n), value_is=0)])
                    
                cache = np.unique(new_cache)
                
                if False and DEBUG:
                    self.plot('filling...')
                
        for i in range(self.ni):
            fill_ext(GPoint(i, 0))
            fill_ext(GPoint(i, self.nj-1))
            
        for j in range(self.nj):
            fill_ext(GPoint(0, j))
            fill_ext(GPoint(self.ni-1, j))
            
        self.a[self.a != -1] = 0
        
        if True and DEBUG:
            self.plot("fill_external")
        
    # ====================================================================================================
    # Extract rectangles
    
    def extract_rects(self):
        
        # ----------------------------------------------------------------------------------------------------
        # A rect candidate status weight:
        # - Number of free cells
        # - Total number of cells
        # Ratio should be maximized
        
        if False and DEBUG:
            self.plot("Extract base", ok_ext=True)

        # ----------------------------------------------------------------------------------------------------
        # A rectangle is acceptable with 3 corners
        
        def rect_is_acceptable(rect):
            #if i1-i0 < 2:
            #    return False
            #if j1 - j0 < 2:
            #    return False
            count = sum([self.is_border(corner) for corner in rect.corners])
            return count >= 3
        
        
        # ----------------------------------------------------------------------------------------------------
        # Find the best rectangle based on a corner
        
        def best_corner_rect(corner):
            
            i0 = self.end_point(corner, LEFT,  cont_value=0).i
            j0 = self.end_point(corner, BOT,   cont_value=0).j
            i1 = self.end_point(corner, RIGHT, cont_value=0).i
            j1 = self.end_point(corner, TOP,   cont_value=0).j
            
            base = GRect(i0, j0, i1, j1)
            
            if False and DEBUG:
                bck = np.array(self.a)
                self[base] = 1
                self.plot("Base")
                self.a = bck
            
            assert(base.surface > 0)
            
            best = base.clone()
            
            for side in range(4):
                for i in range(max(base.length, base.width)):
                    rect = base.move_side(side, i if side in [0, 1] else -i)
                    if rect is None:
                        break
                    
                    if rect_is_acceptable(rect):
                        best = self.best_rect(best, rect)
            
            if False and DEBUG:
                f, t = self.rect_score(best)
                bck = np.array(self.a)
                self.draw_rect(best, 2)
                self.plot(f"score {f}/{t}", ok_ext=True)
                self.a = bck
                
            return best

        # ----------------------------------------------------------------------------------------------------
        # Find best rect while there remain free cells
        
        rects = []
        rect_index = 0
        while np.sum(self.a == 0) > 0:
            
            best = None
            corners = self.get_corners()
            if not len(corners):
                self.plot("NO CORNERS!")
            assert(len(corners))
            
            if False and DEBUG:
                bck = np.array(self.a)
                for corner in corners:
                    self[corner] = 2
                self.plot("Corners")
                self.a = bck
                
            for corner in corners:
                best = self.best_rect(best_corner_rect(corner), best)
                
            rect_index += 1
            self[best] = rect_index
            
            rects.append(best)

            if False and DEBUG:
                f, t = self.rect_score(best)
                self.plot(f"The best {f}/{t}", ok_ext=True)
                
        
        if True and DEBUG:
            self.plot(f"Rectangles", ok_ext=True)
            
        
        return rects
            
            
        
        def left_most(grid, i0, j0):
            for i in reversed(range(1, i0+1)):
                if grid[i-1, j0] != 0:
                    return i
            assert(False)
        
        def right_most(grid, i0, j0):
            for i in range(i0, np.shape(grid)[0] - 2):
                if grid[i+1, j0] != 0:
                    return i
            assert(False)
            
        def bot_most(grid, i0, j0):
            for j in reversed(range(1, j0+1)):
                if grid[i0, j-1] != 0:
                    return j
            assert(False)
            
        def top_most(grid, i0, j0):
            for j in range(j0, np.shape(grid)[1] - 2):
                if grid[i0, j+1] != 0:
                    return j
            assert(False)
            
        def rect_weight(grid, i0, j0, i1, j1):
            count = np.sum(grid[i0:i1+1, j0:j1+1]==0)
            if False and DEBUG:
                dbg = np.array(grid)
                dbg[i0:i1+1, j0:j1+1] = 10
                self.plot(f"rw {i0}, {j0}, {i1}, {j1} -> {count} / {(i1-i0+1)*(j1-j0+1)}", ok_ext=True, grid=dbg)
                
            return count, (i1-i0+1)*(j1-j0+1)
        
        def rect_is_acceptable(grid, cr):
            if i1-i0 < 2:
                return False
            if j1 - j0 < 2:
                return False
            count = sum([is_border(grid, i, j) for i, j in [(i0, j0), (i1, j0), (i1, j1), (i0, j1)]])
            return count >= 3
        
        def find_best_in_direction(grid, i0, j0, i1, j1, direc, min_ratio=.85):
            
            # ----- Rectangle is complete : no better choice
            
            best, best_tot = rect_weight(grid, i0, j0, i1, j1)
            if best == best_tot:
                return i0, j0, i1, j1, best, best_tot
            
            # ----- Explore 

            bi0, bj0, bi1, bj1 = i0, j0, i1, j1
            incr = [(0, 1, 0, 0), (0, 0, -1, 0), (0, 0, 0, -1), (1, 0, 0, 0)][direc]
            
            for i in range(i0, i1+1):
                if not rect_is_acceptable(grid, i, j0, i1, j1):
                    continue
                ok, tot = rect_weight(grid, i, j0, i1, j1)
                if ok/tot > min_ratio and tot > best_tot:
                    best, best_tot = ok, tot
                    bi0, bj0, bi1, bj1 = i, j0, i1, j1
                    break
                
            for i in reversed(range(i0, i1+1)):
                if not rect_is_acceptable(grid, i, j0, i1, j1):
                    continue
                ok, tot = rect_weight(grid, i0, j0, i, j1)
                if ok/tot > min_ratio and tot > best_tot:
                    best, best_tot = ok, tot
                    bi0, bj0, bi1, bj1 = i0, j0, i, j1
                    break
                    
            for j in range(j0, j1+1):
                if not rect_is_acceptable(grid, i0, j, i1, j1):
                    continue
                ok, tot = rect_weight(grid, i0, j, i1, j1)
                if ok/tot > min_ratio and tot > best_tot:
                    best, best_tot = ok, tot
                    bi0, bj0, bi1, bj1 = i0, j, i1, j1
                    break
                
            for j in reversed(range(j0, j1+1)):
                if not rect_is_acceptable(grid, i0, j0, i1, j):
                    continue
                ok, tot = rect_weight(grid, i0, j0, i1, j)
                if ok/tot > min_ratio and tot > best_tot:
                    best, best_tot = ok, tot
                    bi0, bj0, bi1, bj1 = i0, j0, i1, j
                    break
                    
            return bi0, bj0, bi1, bj1, best, best_tot
                    
        
        
            
            
        
        def find_best(grid, i0, j0, i1, j1, min_ratio=.85):
            
            best, best_tot = rect_weight(grid, i0, j0, i1, j1)
            
            if best == best_tot:
                return i0, j0, i1, j1, best, best_tot

            bi0, bj0, bi1, bj1 = i0, j0, i1, j1
            
            for i in range(i0, i1+1):
                if not rect_is_acceptable(grid, i, j0, i1, j1):
                    continue
                ok, tot = rect_weight(grid, i, j0, i1, j1)
                if ok/tot > min_ratio and tot > best_tot:
                    best, best_tot = ok, tot
                    bi0, bj0, bi1, bj1 = i, j0, i1, j1
                    break
                
            for i in reversed(range(i0, i1+1)):
                if not rect_is_acceptable(grid, i, j0, i1, j1):
                    continue
                ok, tot = rect_weight(grid, i0, j0, i, j1)
                if ok/tot > min_ratio and tot > best_tot:
                    best, best_tot = ok, tot
                    bi0, bj0, bi1, bj1 = i0, j0, i, j1
                    break
                    
            for j in range(j0, j1+1):
                if not rect_is_acceptable(grid, i0, j, i1, j1):
                    continue
                ok, tot = rect_weight(grid, i0, j, i1, j1)
                if ok/tot > min_ratio and tot > best_tot:
                    best, best_tot = ok, tot
                    bi0, bj0, bi1, bj1 = i0, j, i1, j1
                    break
                
            for j in reversed(range(j0, j1+1)):
                if not rect_is_acceptable(grid, i0, j0, i1, j):
                    continue
                ok, tot = rect_weight(grid, i0, j0, i1, j)
                if ok/tot > min_ratio and tot > best_tot:
                    best, best_tot = ok, tot
                    bi0, bj0, bi1, bj1 = i0, j0, i1, j
                    break
                    
            return bi0, bj0, bi1, bj1, best, best_tot
        
        
        
        while np.sum(grid==0) > 0:
            
            best_ok, best_tot = None, None
            
            for ic, jc in get_corners(grid):
                
                i0 = left_most(grid, ic, jc)
                j0 = bot_most(grid, ic, jc)
                i1 = right_most(grid, ic, jc)
                j1 = top_most(grid, ic, jc)
                
                bi0, bj0, bi1, bj1, ok, tot = find_best(grid, i0, j0, i1, j1)
                
                if best_ok is None or tot > best_tot:
                    best_ok, best_tot = ok, tot
                    if True and DEBUG:
                        dbg = np.array(grid)
                        dbg[bi0:bi1+1, bj0:bj1+1] = 10
                        self.plot(f"New Best {bi0}, {bj0}, {bi1}, {bj1} -> {best_ok} / {best_tot}", ok_ext=True, grid=dbg)
                        
                    #if best_ok == best_tot:
                    #    break
                    
                    
                    
                    
            index += 1
            grid[bi0:bi1+1, bj0:bj1+1] = index
            
            if False and DEBUG:
                self.plot(f"New rect {best_ok} / {best_tot}: {ok/tot*100:.0f}%", grid=grid, ok_ext=True)
                
            self.rects.append(Rect(bi0-1, bj0-1, bi1, bj1))
        
        self.plot(f"New rect {best_ok} / {best_tot}: {ok/tot*100:.0f}%", grid=grid, ok_ext=True)
        
        
        if True and DEBUG:
            self.rects.plot("Rectangles")
            
        return

    # OLD        
            
    # ====================================================================================================
    # Debug
    
    def plot(self, title="Grid", ok_ext=True, verts=None):
        
        import matplotlib.pyplot as plt
        
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        
        grid = self.a

        ax.plot(0, 0, 'w')
        ax.plot(self.ni, self.nj, 'w')
        
        e = .1
        for i in range(np.shape(grid)[0]):
            for j in range(np.shape(grid)[1]):
                ok = grid[i, j] != 0
                if grid[i, j] < 0 and not ok_ext:
                    ok = False
                if ok:
                    g = grid[i, j]
                    c = 'y' if g < 0 else ['r', 'k', 'c', 'b', 'g'][g%5]
                    ax.plot([i+e, i+1-e, i+1-e, i+e, i+e], [j+e, j+e, j+1-e, j+1-e, j+e], '-' + c, linewidth=.8)
                    
        if verts is not None:
            vs = np.resize(verts - self.origin + (2, 2, 0), (len(verts)+1, 3))
            ax.plot(vs[:, 0], vs[:, 1], ':r')

        plt.title(title)
                    
        plt.show()
        
    @staticmethod
    def test(seed=None):
        
        rng = np.random.default_rng(seed)
        
        count = 5
        
        grid = Grid((30, 30))
        for i in range(count):
            i0 = rng.integers(1, 10)
            j0 = rng.integers(1, 10)
            i1 = rng.integers(i0+1, 29)
            j1 = rng.integers(j0+1, 29)
            
            grid.draw_rect(GRect(i0, j0, i1, j1), i)
            
        #grid.plot()

        grid.fill_external()
        #grid.plot(title=f"Seed {seed}", ok_ext=True)
        
        grid.extract_rects()
        
# ====================================================================================================
# Extract rectangles

def extract_rects(verts):
    
    grid = Grid.FromVerts(verts)
        
    grid.fill_external()

    i_rects = grid.extract_rects()
    
    return grid.rects_to_verts([i_rect.verts() for i_rect in i_rects])

# ====================================================================================================
# Transform a house shape in several rectangles
# When possible...

def simplify(verts, index=None):
    """ Try to simply the external shape of a house into a set of joing rectangles.
    
    The house can be shaped according the followin steps:
        - the contour simplified in a set of joing rectangles
        - each rectangle is elevated randomly
        - terraces and roofs are generated according to the elevations
        
    If the simplification into a set of joining rectangles is not possible,
    the verts are elevated as a single shaped.
    
    Args:
        - verts (array of vertices) : the contour
        - index (int) : house index
        
    Returns:
        - A list of shapes
    """
    
    # ----- Too small
    
    if min(np.max(verts[:, :2], axis=0) - np.min(verts[:, :2], axis=0)) < 2:
        return [verts]
    
    # ----- Segments, lengths and max length
    
    segms   = np.roll(verts, -1, axis=0) - verts
    seg_len = np.linalg.norm(segms, axis=-1)
    
    # ----- Angles of the segments
    
    rad_angles = np.arctan2(segms[:, 1], segms[:, 0])
    
    approx   = 10
    ag_range = 90 // approx
    
    # ----------------------------------------------------------------------------------------------------
    # Determine the main orientation
    #
    # The main orientation is a majority of long segments with the same orientation modulo 90°
    
    # ----- Angles in degrees at the given approximation
    
    angles = np.degrees(rad_angles)
    angles[angles < 0] += 360
    angles = np.round((angles - approx/2)/approx + approx/2).astype(int)
    
    # ----- Weigth the angles with the length of the segments
    
    seg_weights = seg_len/np.sum(seg_len)
    
    dir_weights = [0.]*ag_range      # Direction mod 90
    rot_weights = [0.]*(ag_range*2)  # Direction mod 180 for rotation
    for ag, w in zip(angles, seg_weights):
        dir_weights[ag % ag_range] += w
        rot_weights[ag % (ag_range*2)] += w
        
    # ------ We have a main direction if we have a majority
        
    index = np.argmax(dir_weights)

    # ----------------------------------------------------------------------------------------------------
    # No acceptable simplification
    
    if dir_weights[index] < .7:
        return [verts]
    
    # ----------------------------------------------------------------------------------------------------
    # If we have only 4 sides, this is simple
    
    if len(angles) == 4:
        cag = np.cos(rad_angles[0])
        sag = np.sin(rad_angles[0])
        M    = np.array( ((cag, -sag, 0), (sag, cag, 0), (0, 0, 1)))
        shape_center  = np.average(verts, axis=0)
        rotated_verts = np.einsum('...ij, ...i', M, verts - shape_center)
        
        xs = np.sort(rotated_verts[:, 0])
        ys = np.sort(rotated_verts[:, 1])
        
        x0, x1 = np.average((xs[0], xs[1])), np.average((xs[2], xs[3]))
        y0, y1 = np.average((ys[0], ys[1])), np.average((ys[2], ys[3]))
        
        rotated_verts[0, :2] = (x0, y0)
        rotated_verts[1, :2] = (x1, y0)
        rotated_verts[2, :2] = (x1, y1)
        rotated_verts[3, :2] = (x0, y1)
        
        new_verts = shape_center + np.einsum('...ij, ...i', M.T, rotated_verts)
        
        return [new_verts]
    
    # ----------------------------------------------------------------------------------------------------
    # Let's work on a int grid properly oriented
    
    # ----- We rotate such as the the majority orientation is horizontal
    
    ag_max = np.argmax(rot_weights)
    i_max = None
    for i, ag in enumerate(angles):
        if ag % (2*ag_range) == ag_max:
            i_max = i
            
    # ----- Strange, just in case, let's use the orientation of the longest segment
            
    if i_max is None:
        i_max = np.argmax(seg_len)

    # ----- Rotation
    
    ag  = rad_angles[i_max]
    cag = np.cos(ag)
    sag = np.sin(ag)
    M = np.array( ((cag, -sag, 0), (sag, cag, 0), (0, 0, 1)))
    shape_center = np.average(verts, axis=0)
    
    rotated_verts = np.einsum('...ij, ...i', M, verts - shape_center)
    
    if min(np.max(rotated_verts[:, :2], axis=0) - np.min(rotated_verts[:, :2], axis=0)) < 2:
        return [verts]
    
    # ----------------------------------------------------------------------------------------------------
    # Rectangles extraction through a grid
    
    rects = extract_rects(rotated_verts)

    # ----- Rotation
    
    return [shape_center + np.einsum('...ij, ...i', M.T, rect) for rect in rects]



        
        
if __name__ == '__main__':
    
    import matplotlib.pyplot as plt
    
    verts = np.zeros((6, 3), float)
    verts[0] = (1.1,  3.5, 0)
    verts[1] = (9.4,  3.7, 0)
    verts[2] = (9.6, 12.5, 0)
    verts[3] = (5.7, 12.0, 0)
    verts[4] = (5.7,  7.1, 0)
    verts[5] = ( .9,  7.1, 0)
    
    rects = extract_rects(verts)
    
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    
    vs = np.resize(verts, (len(verts)+1, 3))
    ax.plot(vs[:, 0], vs[:, 1], '-k')
    
    for rect in rects:
        vs = np.resize(rect, (len(rect)+1, 3))
        ax.plot(vs[:, 0], vs[:, 1], '-')
        
    
    plt.title(f"Test")
    plt.show()


