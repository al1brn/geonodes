#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 05:13:23 2023

@author: alain
"""

import numpy as np

# ====================================================================================================
# A house is a set of walls/segments
#
# The segments come from rectangles

class Segment:
    def __init__(self, i0, i1, other_dim, hrz, owner):
        """ A range of integer points forming an horizontal of vertical segment.
        
        A segment is oriented, the ending index can be less than the starting index.
        The orientation is considered as positive if the indices grow from start to end
        or negative in the oppositie case.
        
        Args:
            - i0 (int) : starting index of the segment
            - i1 (int) : ending index of the segment. Can't be equal to the starting index
            - other_dim (int) : index in the other dimension
            - hrz (bool) : horizontal (True) or vertical (False) segment
            - owner (any) : index to a owner, for instance the rectangle index in a Rects list.
        """
        
        assert(i0 != i1)

        self.i0  = i0
        self.i1  = i1
        self.o   = other_dim
        self.hrz = hrz
        
        self.owner = owner
        
    def __str__(self):
        return f"<{'H' if self.hrz else 'V'} Segment [{self.i0:2d}  {self.i1:2d}] @ {self.o:2d}, owner: {self.owner}>"

    def __repr__(self):
        return f"<{'H' if self.hrz else 'V'} Segment @ {self.o:2d}: {self.i0:2d} -> {self.i1:2d} = {self.arange}>"
    
    @property
    def abs_hash(self):
        return f"{min(self.i0, self.i1)}.{max(self.i0, self.i1)}.{self.o}.{1 if self.hrz else 0}"

    @property
    def sgn_hash(self):
        return f"{self.i0}.{self.i1}.{self.o}.{1 if self.hrz else 0}"
        
    
    @property
    def is_positive(self):
        """ Positive segment.
        
        Returns:
            - bool : True if ending index is less than starting index.
        """
        return self.i1 > self.i0
    
    @property
    def is_negative(self):
        """ Negative segment.
        
        Returns:
            - bool : True if ending index is greater than starting index.
        """
        return self.i1 < self.i0
    
    def opposite(self):
        return Segment(self.i1, self.i0, self.o, self.hrz, self.owner)
    
    @property
    def corners(self):
        """ The coordnates of the extremities of the segment.
        
        Returns:
            - couple of ints : the coordinates of the extremities.
        """
        if self.hrz:
            return (self.i0, self.o), (self.i1, self.o)
        else:
            return (self.o, self.i0), (self.o, self.i1)
        
    @property
    def length(self):
        return self.i1 - self.i0
        
    @property
    def arange(self):
        """ List of the indices forming the segment.
        
        The indices are arranged from starting to ending index:
            
        ``` python
        segm = Segment(10, 5, True, 0, None)
        print(segm.arange)
        # [10, 9, 8, 7,6, 5]
        
        Returns:
            - np.ndarray : the indices from starting index to ending index
        """
        return np.arange(self.i0, self.i1+1) if self.is_positive else -np.arange(-self.i0, -self.i1+1)
    
    def contains(self, i):
        """ The segment constains an index.
        
        Returns:
            - bool : True if i is in the segment.
        """
        return i in self.arange
        
    def is_aligned_with(self, segment):
        """ Is the segment aligned with another one.
        
        Two segments are aligned when:
            - they share the same direction horizontal or vertical
            - they share the same index in the other direction
            
        Returns:
            - bool : True if the segments are aligned
        """
        return self.hrz == segment.hrz and self.o == segment.o
    
    @property
    def i_min(self):
        """ Minimum index.
        
        Returns:
            - int : minimum index
        """
        return min(self.i0, self.i1)
    
    @property
    def i_max(self):
        """ Maximum index.
        
        Returns:
            - int : maximum index
        """
        return max(self.i0, self.i1)
    
    def is_same_as(self, line):
        """ Compare two segments independantly of their orientation.
        
        Returns:
            bool : True if the segments are aligned and their extremities are identical.
        """
        return self.hrz == line.hrz and self.o == line.o and self.i_min == line.i_min and self.i_max == line.i_max
    
    def follows(self, segment):
        """ Test if a segment follows another one.
        
        If the segment have the same orientation (hrz), one is following the other
        if it starts by the end of the other one.
        If the segments are perpendicular, the index if the other direction must be tested.
        
        Returns:
            - bool : True if the segment follows the other one
        """
        
        if self.hrz == segment.hrz:
            return self.o == segment.o and self.i0 == segment.i1
        else:
            return self.o == segment.i1 and self.i0 == segment.o
    
    # ----------------------------------------------------------------------------------------------------
    # Split
    
    def split(self, i0, i1):
        """ Split the segment..
        
        The two indices are the two extremities of the segment to create.
        These indices must be inside the segment.
        
        The orientation positive or negative of the created segments is the one of the current segment,
        independantly of the orientation of the couple of argugments (i0, i1).
        
        If the arguments match the extremities of the segment, no segment is created, otherwise
        one or two segments are created such as all the segments follow each other for form
        the initial segment.
        
        Note that the arguments are typically the result of the method 'overlaps_with':
            
        ``` python
        i0, i1 = segment.overlaps_with(other)
        if i0 is not None:
            new_segments = segment.split(i0, i1)
            # the segments in the list new_segments can replace segment
        ``` 
        
        Args:
            - i0 : one extremity of the segment to create
            - i1 : the other extremity of the segment to create
            
        Returns:
            - lis of Segments : 1 to 3 successive segments forming the current segment
        """
        
        if self.is_positive:
            i0_ = min(i0, i1)
            i1_ = max(i0, i1)
            assert(i0_>=self.i0 and i1_<=self.i1)
            
        else:
            i0_ = max(i0, i1)
            i1_ = min(i0, i1)
            assert(i1_>=self.i1 and i0_<=self.i0)

        res = []

        if i0_ != self.i0:
            res.append(Segment(self.i0, i0_, self.o, self.hrz, self.owner))
            
        res.append(Segment(i0_, i1_, self.o, self.hrz, self.owner))
        
        if i1_ != self.i1:
            res.append(Segment(i1_, self.i1, self.o, self.hrz, self.owner))
            
        return res

    # ----------------------------------------------------------------------------------------------------
    # Overlapping lines

    def overlaps_with(self, segment):
        """ Test if two segments overlap.

        The indices returned by the method can be used in the method 'split' to create succesive
        segments with the orverlapping section as a "shared" segment.
        
        When two segments overalap, each one can be replaced by a succession of segments, for example:
            - segment A : [5, 6, 7, 8, 9]
            - segment B : [7, 6, 5, 4, 3]
            - they overlap in [5, 6, 7] given by indices 5, 7
            - segment A is replaced by two segments : [5, 6, 7] and [8, 9]
            - segment B is replaced by two segments : [7, 6, 5] and [4, 3]
            
        By creating independant segments for the overlapping sections of two segments, we identify
        the inside parts of a house. The not overlapping segments form the external shape of the house.
        
        Use the method 'same_as' to identify the overlapping segment.
        
        Args:
            - segment (Segment) : the other segement
            
        Returns:
            - couple of ints or (None, None) : overlapping extremining if the segments share a section, (None, None) other wise
        """
        
        if not self.is_aligned_with(segment) or self.is_same_as(segment):
            return None, None
        
        a = np.intersect1d(self.arange, segment.arange)
        
        if len(a) > 1:
            i0 = np.min(a)
            i1 = np.max(a)
            
            return i0, i1
            
            #return self.split(i0, i1), line.split(i0, i1)
            
            #return Segment(i0, i1+1, self.o, self.hrz) if self.is_positive else Segment(i1, i0-1, self.o, self.hrz)
        else:
            return None, None
        
# ====================================================================================================
# A network of segments
        
class Segments(list):
    
    def __init__(self, segments=None):
        """ A list of segments.
        
        Note that the order of the segments in the list can be meaningful or not, depending
        on the way the list is built.
        
        If it is built as a contour, each segment follows the previous one to form a closed shape.
        It can simply be a list of segments.
        
        This classes provides features to manage the 'owner' attribute of a segment. It uses it
        as the index of the list of rectangle. The methode 'max_owner' gives the maximum value of 
        the 'owner' attribute, giving a way to increment the value when a new rectangle is added.
        
        The 'owner' attribute provides a way to select segments belonging to a rectangle.
        
        Args:
            - segments (list of Segment = None) : the segments to initialize the list with.
        """
        super().__init__()
        if segments is not None:
            self.extend(segments)
    
    # ----------------------------------------------------------------------------------------------------
    # Initialize from a rectangle
    
    @classmethod
    def FromRect(cls, rect, index=0):
        """ Create a new list from a rectangle.
        
        Args:
            - rect (Rect) : rectangle giving the four segments to add.
            - index (int=0) : index of the rectrangle
            
        Returns:
            - Segments : a list of 4 segments
        """
        
        return cls([
                Segment(rect.i0, rect.i1, rect.j0, True,  owner=index),
                Segment(rect.j0, rect.j1, rect.i1, False, owner=index),
                Segment(rect.i1, rect.i0, rect.j1, True,  owner=index),
                Segment(rect.j1, rect.j0, rect.i0, False, owner=index),
            ])
    
    @classmethod
    def FromRects(cls, rects):
        segments = cls()
        for rect in rects:
            segments.add_rect(rect)
        return segments
        
    def __str__(self):
        return f"<Segments: {len(self)}>"
    
    def __repr__(self):
        s = f"<Segments: {len(self)}:"
        for i_line, line in enumerate(self):
            sibs = self.siblings(i_line)
            s += f"\n{i_line:3d}: {str(self.siblings(i_line)):5s} {str(line)}"
        return s + "\n>"
    
    # ----------------------------------------------------------------------------------------------------
    # Add segments
    
    def add_segments(self, other_segments):
        """ Add other segments, indentifying the overlaps.
        
        The segments added can overlap with the existing segments. This method splits
        the overlapping segments before inserting them in the list.
        
        The simpler case is when two segments overlap:
            - in the current list, the segment is replaced by 1 to 3 segments including
              the overlapping section
            - the same is done in the other list
            - the two lists are merged
            
        But more complex cases can occur: a segment in one list can overlap with more than
        one segment in the other one. Moreover, one of these overlapping segment can, on its turn,
        overlaps with more than one segment in the current list.
        
        As a consequence, each time an overlap is detected and that, consequently, new segments
        are created to replace overlapping ones, the comparizon one by one restarts from the 
        begining to take the new segments into account.
        
        Args:
            - other_segments (Segments) : segments to add
        """
        
        # ----- Easy : the current list is empty

        if len(self) == 0:
            self.extend(other_segments)
            return
        
        # ----- Loop while a split is performed
        # each line can overlap one or more times with one or more other segment.
        # and vice versa!...
        
        # Let's work on a copy to keep the argument unchanged
        
        others = Segments(other_segments)
        
        loop_again = True
        while loop_again:
            
            loop_again = False
            
            # ----- Double loop to compare each one with each other one
            
            for i_segm, segm in enumerate(self):
                for i_other, other in enumerate(others):
                    
                    # Do he two segments overlap ?
                    i0, i1 = segm.overlaps_with(other)
                    
                    # Yes : we split and restart the loops from the begining
                    if i0 is not None:
                        
                        del self[i_segm]
                        self.extend(segm.split(i0, i1))
                        
                        del others[i_other]
                        others.extend(other.split(i0, i1))
                        
                        loop_again = True
                        break
                    
                if loop_again:
                    break
                
        # ----- We include the new segments properly split
                    
        self.extend(others)

    # ----------------------------------------------------------------------------------------------------
    # Merge a rect
    
    @property
    def max_owner(self):
        """ Max value of the segments *owner* attribute.
        
        ```max_value+1``` gives the number of rectangles included in the list.
        
        Returns:
            - int : max *owner* in the list of segments.
        """
        if len(self) == 0:
            return -1
        else:
            return max([segm.owner for segm in self])
    
    def add_rect(self, rect):
        """ Merge a new rectangle.
        
        Args:
            - rect (Rect) : the rectangle to add
        """
        self.add_segments(Segments.FromRect(rect, index=self.max_owner + 1))
        
    # ----------------------------------------------------------------------------------------------------
    # A line can exist several times
    
    def siblings(self, index):
        """ Get the identical segments indices.
        
        This gives the overlapping segments. It uses the method ```Segment.same_as``` 
        
        Args:
            - index (int) : index of the segment to get the siblings of
        Returns:
            - list of ints : the indices of the identical segments.
        """
        segment = self[index]
        res = []
        for i, other in enumerate(self):
            if i != index and segment.is_same_as(other):
                res.append(i)
        return res
    
    # ----------------------------------------------------------------------------------------------------
    # Pick a follower in a list
    
    def pick_next(self, segments):
        """ Pick a segment which follows the last segment in the list.
        
        This method is used to build the external contours from a list of segments:
            - A new instance of Segments is initialized with segment chosen in the initiali list
            - Call `pick_next` until the contour is closed
            
        The contour is closed once the first segment follows the last one.    
        All the segments, including the initial one, must have no sibling. No test is performed,
        the provided list is supposed to contain only external segments
        
        If the liste is closed, no segment is picked. The caller must create a new contour if
        segments remain in the list.
        
        **NOTE** : the segment picked in the provided list is removed from this list. Make sur
        to work with a copy if the list is still need.
        
        Args:
            - segments (Segments) : the list of segment to select a segment from.
        Returns:
            - bool : True if a segment has been picked, False otherwise
        """
        
        # ----- Already closed: no more segment
        
        if self.is_closed:
            return False
        
        # ----- Select an index
        
        index = None
        if len(self) == 0:
            index = 0
        else:
            for i_segm, segm in enumerate(segments):
                if segm.follows(self[-1]):
                    index = i_segm
                    break
                
        # ----- Transfer the selected segment
                
        if index is None:
            return False
        
        else:
            self.append(segments[index])
            del segments[index]
            return True
        
    @property
    def is_closed(self):
        """ Test if the list forms a closed shape.
        
        Meaningful only when building the list by addint succesive segments, typically calling 'pick_next' method.
        
        Returns:
            - bool : True if the contour is closed, False otherwise
        """
        if len(self) < 4:
            return False
        else:
            return self[0].follows(self[-1])
        
    # ----------------------------------------------------------------------------------------------------
    # Contours
    
    def contours(self):
        """ Build the external contours of a list of segments.
        
        External contours are formed by the segments which belong only to one rectangle, i.e. which
        don't come from overlapping sections of segments.
        
        The first step consists in extracting the external segments. They are in an arbitrary order.
        Then a first contour is built by selecing one segment an picking the next one in the remainging list.
        
        The process restarts while segments remain in the list.
        
        Returns:
            - list of Segments : the contours
        """
        
        # ----- First, let's build the list of external segments
        
        borders = []
        for i_line, line in enumerate(self):
            if len(self.siblings(i_line)) == 0:
                borders.append(line)

        if len(borders) == 0:
            return None
        
        # ---- Build build contours one by one, while segments remain in the borders list
        
        contours = []
        
        while len(borders) > 0:
            new_contour = True
            for contour in contours:
                if contour.pick_next(borders):
                    new_contour = False
                    break
                    
            if new_contour:
                contour = Segments()
                contour.append(borders[0])
                del borders[0]
                contours.append(contour)
                
        for contour in contours:
            assert(contour.is_closed)
                
        return contours
    
    # ----------------------------------------------------------------------------------------------------
    # Rect contours
    
    def rect_contour(self, index):
        """ Build the contour of a rectangle.
        
        Args:
            - index (int) : value of the 'owner' Segment attribute
        Returns:
            - Segments : the contour of the rectangle
        """
        segments = Segments([segm for segm in self if segm.owner == index])
        return segments.contours()[0]
    
    
    # ====================================================================================================
    # Back to true vertices

    # ----------------------------------------------------------------------------------------------------
    # Corner
    
    @property
    def corners(self):
        """ List of 2D corners of the shape.
        
        Meaningful solely for contours
        
        Returns:
            - list of couples of int : the coordinates of the corners
        """
        return [line.corners[0] for line in self]
    
    @property
    def bounds(self):
        """ Bounds of the segments
        
        Returns:
            - 4 floats : x min, y min, x max, y max
        """
        corners = np.array(self.corners)
        c_min = np.min(corners, axis=0)
        c_max = np.max(corners, axis=0)
        return c_min[0], c_min[1], c_max[0], c_max[1]
    
    @property
    def surface(self):
        """ The surface of the bounds rectangle.
        
        Meaningful solely for rectangular contours.

        Returns:
            - float
        """
        x0, y0, x1, y1 = self.bounds
        return (x1 - x0)*(y1 - y0)

                
    # ====================================================================================================
    # Debug
                
    def plot(self, title="Segments"):
        
        print("---------- PLOT:", title)
        print(repr(self))
        print()
        
        import matplotlib.pyplot as plt
        
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        
        ax.plot((0, 20), (0, 20), 'w')
        
        for i_line, line in enumerate(self):
            p0, p1 = line.corners
            mode = '-k' if len(self.siblings(i_line)) == 0 else '-r'
            ax.plot( (p0[0], p1[0]), (p0[1], p1[1]), mode)
        
        #ax.plot( (p0[0], p1[0]), (p0[1], p1[1]), '-k')
        
        plt.title(title)
        plt.show()
        
    def plot_contours(self, title="Contours"):
        
        import matplotlib.pyplot as plt
        
        contours = self.contours()

        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        
        ax.plot((0, 20), (0, 20), 'w')
        
        for i_contour, contour in enumerate(contours):
            
            c = ['k', 'c', 'b', 'y', 'g', 'r'][i_contour % 6]
             
            for i_line, line in enumerate(contour):
                p0, p1 = line.corners
                ax.plot( (p0[0], p1[0]), (p0[1], p1[1]), '-' + c)
        
        plt.title(title)
        plt.show()
        
        
    @staticmethod
    def debug1():

        class Rect:
            def __init__(self, i0, j0, i1, j1):
                self.i0, self.j0, self.i1, self.j1 = i0, j0, i1, j1
            
            
        for i0 in [3, 6, 9]:
            for i1 in [11, 16, 20]:
                
                if True:
                    cont = Segments.FromRect(Rect(6, 6, 16, 16))
                    rect = Rect(i0, 1, i1, 6)
                    name = f"BOT {i0} {i1}"
                    print(name, cont.add_rect(rect))
                    print(cont)
                    cont.plot(name) 
                    cont.plot_contours(name) 
                    
                if True:
                    cont = Segments.FromRect(Rect(6, 6, 16, 16))
                    rect = Rect(16, i0, 20, i1)
                    name = f"RGT {i0} {i1}"
                    print(name, cont.add_rect(rect))
                    print(cont)
                    cont.plot(name) 
                    cont.plot_contours(name) 
                    
                if True:
                    cont = Segments.FromRect(Rect(6, 6, 16, 16))
                    rect = Rect(i1, 20, i0, 16)
                    name = f"TOP {i0} {i1}"
                    print(name, cont.add_rect(rect))
                    print(cont)
                    cont.plot(name) 
                    cont.plot_contours(name) 
                
                if True:
                    cont = Segments.FromRect(Rect(6, 6, 16, 16))
                    rect = Rect(3, i0, 6, i1)
                    name = f"LFT {i0} {i1}"
                    print(name, cont.add_rect(rect))
                    print(cont)
                    cont.plot(name) 
                    cont.plot_contours(name) 

if __name__ == '__main__':
    Segments.debug1()