#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 08:10:09 2022

@author: alain
"""
try:
    import bpy
except:
    pass

DIMS = {
    'NodeFrame'                               : (300.0000, 200.0000),
    'FunctionNodeAlignEulerToVector'          : (280.0000, 468.0000),
    'FunctionNodeBooleanMath'                 : (280.0000, 254.0000),
    'FunctionNodeCompare'                     : (280.0000, 308.0000),
    'FunctionNodeFloatToInt'                  : (280.0000, 210.0000),
    'FunctionNodeInputBool'                   : (280.0000, 160.0000),
    'FunctionNodeInputColor'                  : (280.0000, 370.0000),
    'FunctionNodeInputInt'                    : (280.0000, 160.0000),
    'FunctionNodeInputSpecialCharacters'      : (280.0000, 144.0000),
    'FunctionNodeInputString'                 : (280.0000, 160.0000),
    'FunctionNodeInputVector'                 : (280.0000, 240.0000),
    'FunctionNodeRandomValue'                 : (280.0000, 586.0000),
    'FunctionNodeReplaceString'               : (280.0000, 238.0000),
    'FunctionNodeRotateEuler'                 : (280.0000, 428.0000),
    'FunctionNodeSliceString'                 : (280.0000, 238.0000),
    'FunctionNodeStringLength'                : (280.0000, 150.0000),
    'FunctionNodeValueToString'               : (280.0000, 194.0000),
    'GeometryNodeAccumulateField'             : (280.0000, 516.0000),
    'GeometryNodeAttributeDomainSize'         : (280.0000, 346.0000),
    'GeometryNodeAttributeStatistic'          : (280.0000, 656.0000),
    'GeometryNodeAttributeTransfer'           : (280.0000, 356.0000),
    'GeometryNodeBoundBox'                    : (280.0000, 238.0000),
    'GeometryNodeCaptureAttribute'            : (280.0000, 356.0000),
    'GeometryNodeCollectionInfo'              : (280.0000, 298.0000),
    'GeometryNodeConvexHull'                  : (280.0000, 150.0000),
    'GeometryNodeCurveArc'                    : (280.0000, 966.0000),
    'GeometryNodeCurveEndpointSelection'      : (280.0000, 194.0000),
    'GeometryNodeCurveHandleTypeSelection'    : (280.0000, 210.0000),
    'GeometryNodeCurveLength'                 : (280.0000, 150.0000),
    'GeometryNodeCurvePrimitiveBezierSegment' : (280.0000, 866.0000),
    'GeometryNodeCurvePrimitiveCircle'        : (280.0000, 258.0000),
    'GeometryNodeCurvePrimitiveLine'          : (280.0000, 498.0000),
    'GeometryNodeCurvePrimitiveQuadrilateral' : (280.0000, 258.0000),
    'GeometryNodeCurveQuadraticBezier'        : (280.0000, 642.0000),
    'GeometryNodeCurveSetHandles'             : (280.0000, 304.0000),
    'GeometryNodeCurveSpiral'                 : (280.0000, 370.0000),
    'GeometryNodeCurveSplineType'             : (280.0000, 254.0000),
    'GeometryNodeCurveStar'                   : (280.0000, 326.0000),
    'GeometryNodeCurveToMesh'                 : (280.0000, 238.0000),
    'GeometryNodeCurveToPoints'               : (280.0000, 390.0000),
    'GeometryNodeDeleteGeometry'              : (280.0000, 304.0000),
    'GeometryNodeDistributePointsOnFaces'     : (340.0000, 430.0000),
    'GeometryNodeDualMesh'                    : (280.0000, 194.0000),
    'GeometryNodeDuplicateElements'           : (280.0000, 342.0000),
    'GeometryNodeExtrudeMesh'                 : (280.0000, 474.0000),
    'GeometryNodeFieldAtIndex'                : (280.0000, 312.0000),
    'GeometryNodeFillCurve'                   : (280.0000, 210.0000),
    'GeometryNodeFilletCurve'                 : (280.0000, 298.0000),
    'GeometryNodeFlipFaces'                   : (280.0000, 194.0000),
    'GeometryNodeGeometryToInstance'          : (320.0000, 150.0000),
    'GeometryNodeGroup'                       : (280.0000, 100.0000),
    'GeometryNodeImageTexture'                : (480.0000, 392.0000),
    'GeometryNodeInputCurveHandlePositions'   : (300.0000, 194.0000),
    'GeometryNodeInputCurveTilt'              : (280.0000, 100.0000),
    'GeometryNodeInputID'                     : (280.0000, 100.0000),
    'GeometryNodeInputIndex'                  : (280.0000, 100.0000),
    'GeometryNodeInputMaterial'               : (280.0000, 160.0000),
    'GeometryNodeInputMaterialIndex'          : (280.0000, 100.0000),
    'GeometryNodeInputMeshEdgeAngle'          : (280.0000, 144.0000),
    'GeometryNodeInputMeshEdgeNeighbors'      : (280.0000, 100.0000),
    'GeometryNodeInputMeshEdgeVertices'       : (280.0000, 232.0000),
    'GeometryNodeInputMeshFaceArea'           : (280.0000, 100.0000),
    'GeometryNodeInputMeshFaceIsPlanar'       : (280.0000, 150.0000),
    'GeometryNodeInputMeshFaceNeighbors'      : (300.0000, 144.0000),
    'GeometryNodeInputMeshIsland'             : (280.0000, 144.0000),
    'GeometryNodeInputMeshVertexNeighbors'    : (280.0000, 144.0000),
    'GeometryNodeInputNamedAttribute'         : (280.0000, 214.0000),
    'GeometryNodeInputNormal'                 : (280.0000, 100.0000),
    'GeometryNodeInputPosition'               : (280.0000, 100.0000),
    'GeometryNodeInputRadius'                 : (280.0000, 100.0000),
    'GeometryNodeInputSceneTime'              : (280.0000, 144.0000),
    'GeometryNodeInputShadeSmooth'            : (280.0000, 100.0000),
    'GeometryNodeInputSplineCyclic'           : (280.0000, 100.0000),
    'GeometryNodeInputSplineResolution'       : (280.0000, 100.0000),
    'GeometryNodeInputTangent'                : (280.0000, 100.0000),
    'GeometryNodeInstanceOnPoints'            : (280.0000, 654.0000),
    'GeometryNodeInstancesToPoints'           : (280.0000, 282.0000),
    'GeometryNodeIsViewport'                  : (280.0000, 100.0000),
    'GeometryNodeJoinGeometry'                : (280.0000, 150.0000),
    'GeometryNodeMaterialSelection'           : (280.0000, 150.0000),
    'GeometryNodeMergeByDistance'             : (280.0000, 298.0000),
    'GeometryNodeMeshBoolean'                 : (280.0000, 342.0000),
    'GeometryNodeMeshCircle'                  : (280.0000, 254.0000),
    'GeometryNodeMeshCone'                    : (280.0000, 562.0000),
    'GeometryNodeMeshCube'                    : (280.0000, 402.0000),
    'GeometryNodeMeshCylinder'                : (280.0000, 518.0000),
    'GeometryNodeMeshGrid'                    : (280.0000, 282.0000),
    'GeometryNodeMeshIcoSphere'               : (280.0000, 194.0000),
    'GeometryNodeMeshLine'                    : (280.0000, 538.0000),
    'GeometryNodeMeshToCurve'                 : (280.0000, 194.0000),
    'GeometryNodeMeshToPoints'                : (280.0000, 342.0000),
    'GeometryNodeMeshUVSphere'                : (280.0000, 238.0000),
    'GeometryNodeObjectInfo'                  : (280.0000, 386.0000),
    'GeometryNodePointsToVertices'            : (280.0000, 194.0000),
    'GeometryNodePointsToVolume'              : (340.0000, 342.0000),
    'GeometryNodeProximity'                   : (280.0000, 298.0000),
    'GeometryNodeRaycast'                     : (300.0000, 736.0000),
    'GeometryNodeRealizeInstances'            : (280.0000, 150.0000),
    'GeometryNodeRemoveAttribute'             : (340.0000, 194.0000),
    'GeometryNodeReplaceMaterial'             : (280.0000, 238.0000),
    'GeometryNodeResampleCurve'               : (280.0000, 302.0000),
    'GeometryNodeReverseCurve'                : (280.0000, 194.0000),
    'GeometryNodeRotateInstances'             : (280.0000, 566.0000),
    'GeometryNodeSampleCurve'                 : (280.0000, 342.0000),
    'GeometryNodeScaleElements'               : (280.0000, 396.0000),
    'GeometryNodeScaleInstances'              : (280.0000, 566.0000),
    'GeometryNodeSeparateComponents'          : (280.0000, 326.0000),
    'GeometryNodeSeparateGeometry'            : (280.0000, 298.0000),
    'GeometryNodeSetCurveHandlePositions'     : (280.0000, 462.0000),
    'GeometryNodeSetCurveRadius'              : (280.0000, 238.0000),
    'GeometryNodeSetCurveTilt'                : (280.0000, 238.0000),
    'GeometryNodeSetID'                       : (280.0000, 238.0000),
    'GeometryNodeSetMaterial'                 : (280.0000, 238.0000),
    'GeometryNodeSetMaterialIndex'            : (280.0000, 238.0000),
    'GeometryNodeSetPointRadius'              : (280.0000, 238.0000),
    'GeometryNodeSetPosition'                 : (280.0000, 402.0000),
    'GeometryNodeSetShadeSmooth'              : (280.0000, 238.0000),
    'GeometryNodeSetSplineCyclic'             : (280.0000, 238.0000),
    'GeometryNodeSetSplineResolution'         : (280.0000, 238.0000),
    'GeometryNodeSplineLength'                : (280.0000, 144.0000),
    'GeometryNodeSplineParameter'             : (280.0000, 188.0000),
    'GeometryNodeSplitEdges'                  : (280.0000, 194.0000),
    'GeometryNodeStoreNamedAttribute'         : (280.0000, 352.0000),
    'GeometryNodeStringJoin'                  : (280.0000, 194.0000),
    'GeometryNodeStringToCurves'              : (380.0000, 722.0000),
    'GeometryNodeSubdivideCurve'              : (280.0000, 194.0000),
    'GeometryNodeSubdivideMesh'               : (280.0000, 194.0000),
    'GeometryNodeSubdivisionSurface'          : (300.0000, 348.0000),
    'GeometryNodeSwitch'                      : (280.0000, 298.0000),
    'GeometryNodeTransform'                   : (280.0000, 642.0000),
    'GeometryNodeTranslateInstances'          : (280.0000, 402.0000),
    'GeometryNodeTriangulate'                 : (280.0000, 348.0000),
    'GeometryNodeTrimCurve'                   : (280.0000, 302.0000),
    'GeometryNodeViewer'                      : (280.0000, 144.0000),
    'GeometryNodeVolumeToMesh'                : (340.0000, 298.0000),
    'NodeGroupInput'                          : (280.0000, 144.0000),
    'NodeGroupOutput'                         : (280.0000, 144.0000),
    'NodeReroute'                             : (16.0000, 16.0000),
    'ShaderNodeClamp'                         : (280.0000, 298.0000),
    'ShaderNodeCombineRGB'                    : (280.0000, 238.0000),
    'ShaderNodeCombineXYZ'                    : (280.0000, 238.0000),
    'ShaderNodeFloatCurve'                    : (480.0000, 584.0000),
    'ShaderNodeMapRange'                      : (280.0000, 970.0000),
    'ShaderNodeMath'                          : (280.0000, 264.0000),
    'ShaderNodeMixRGB'                        : (280.0000, 342.0000),
    'ShaderNodeRGBCurve'                      : (480.0000, 584.0000),
    'ShaderNodeSeparateRGB'                   : (280.0000, 238.0000),
    'ShaderNodeSeparateXYZ'                   : (280.0000, 358.0000),
    'ShaderNodeTexBrick'                      : (300.0000, 780.0000),
    'ShaderNodeTexChecker'                    : (280.0000, 326.0000),
    'ShaderNodeTexGradient'                   : (280.0000, 254.0000),
    'ShaderNodeTexMagic'                      : (280.0000, 342.0000),
    'ShaderNodeTexMusgrave'                   : (300.0000, 440.0000),
    'ShaderNodeTexNoise'                      : (280.0000, 430.0000),
    'ShaderNodeTexVoronoi'                    : (280.0000, 490.0000),
    'ShaderNodeTexWave'                       : (300.0000, 618.0000),
    'ShaderNodeTexWhiteNoise'                 : (280.0000, 258.0000),
    'ShaderNodeValToRGB'                      : (480.0000, 424.0000),
    'ShaderNodeValue'                         : (280.0000, 160.0000),
    'ShaderNodeVectorCurve'                   : (480.0000, 704.0000),
    'ShaderNodeVectorMath'                    : (280.0000, 338.0000),
    'ShaderNodeVectorRotate'                  : (280.0000, 636.0000),

}


# ====================================================================================================
# A box as a size and links to other boxes
# inherdited classes must implement the properties
# - x
# - y
# - height
# - width
# The muts inititalize inputs and outputs with other boxes
# The parent is a list of boxes

class Box(list):
    
    unique_id = 0
    all_links = []
    
    H_MARGIN = 40
    V_MARGIN = 40
    V_STEP   = 20
    
    # ---------------------------------------------------------------------------
    # Initialization
    
    def __init__(self):
        super().__init__()
        Box.unique_id += 1
        
        self.id       = Box.unique_id
        self.name     = "Box"
        self.parent   = None
        self.depth_   = 0
        self.inf_loop = False
        
    def __eq__(self, other):
        return self.id == other.id
    
    def update(self):
        pass

    # ---------------------------------------------------------------------------
    # Display
        
    def __repr__(self):
        return f"[{self.name} - {self.id}]" 
    
    def dump(self, prof=0):
        print("   "*prof, self, "IO:", (len(self.inputs), len(self.outputs)), self.depth)
        for box in self:
            box.dump(prof+1)
            
    def dump_io(self):
        print('-'*20)
        print("Box", self)
        print("   Inputs:")
        for b in self.inputs:
            print("      ", b)
        print("   Outputs:")
        for b in self.outputs:
            print("      ", b)
        print()
    
    @staticmethod
    def dump_links():
        print("-"*30)
        print("Links:")
        for i, link in enumerate(Box.all_links):
            s0 = f"{link[0]}"
            s1 = f"{link[1]}"
            print(f"{i:2d}: {s0:30s} --> {s1}")
        print()
    
            
    @property
    def is_top(self):
        return self.parent is None
        
    @property
    def depth(self):
        return self.depth_
    
    @depth.setter
    def depth(self, value):
        if self.inf_loop:
            return
            raise RuntimeError(f"Infinite loop on {self}")
            
        self.inf_loop = True
            
        self.depth_ = max(self.depth_, value)
        for box in self.inputs:
            box.depth = self.depth + 1
            
        self.inf_loop = False

    # ===========================================================================
    # The links are managed in an array to ease the changes
    
    @staticmethod
    def link(box0, box1):
        Box.all_links.append([box0, box1])
        
        
    @property
    def inputs(self):
        inputs = []
        for link in Box.all_links:
            if link[1] == self:
                if link[0] not in inputs:
                    inputs.append(link[0])
                    
        return inputs

    @property
    def outputs(self):
        outputs = []
        for link in Box.all_links:
            if link[0] == self:
                if link[1] not in outputs:
                    outputs.append(link[1])

        return outputs
            
    # ===========================================================================
    # Update the links
    # Once the boxes are placed within a frame, the frame capture the links
    # towards the exterior
    
    def update_frame_links(self):

        for box in self:
            
            # ----- The box can have children
            # The links must be updated first
            
            box.update_frame_links()
            
            # ----- All children links are given to the owner
            # if they leave the frame

            if not self.is_top:
            
                for link in Box.all_links:
                    if link[0] == box:
                        if link[1].parent != self:
                            link[0] = self
    
                    if link[1] == box:
                        if link[0].parent != self:
                            link[1] = self
            
    # ===========================================================================
    # Arrange its children
    
    def arrange_children(self):
        
        if len(self) == 0:
            return

        # ----- Arrange the sub children
        
        for box in self:
            box.arrange_children()
            
        # ----- The nodes with no outputs within the frame
        
        tops = []
        for box in self:
            if len(box.outputs) == 0:
                tops.append(box)
                
        # ----- Compute the depths
        
        for box in tops:
            box.depth = 0
            
        # ----- Max depth will give the number of columns
        
        max_depth = 0
        for box in self:
            max_depth = max(max_depth, box.depth)

        # ----- Build the columns width their size
            
        cols_count  = max_depth + 1
        cols        = []
        cols_width  = []
        cols_height = []
        for i_col in range(cols_count):
            col = []
            w   = 0
            h   = 0
            for box in self:
                if box.depth == i_col:
                    col.append(box)
                    w = max(w, box.width)
                    h += box.height
                    
            cols.append(col)
            cols_width.append(w)
            cols_height.append(h)
            
        # ----- Place the boxes vertically
        
        for i_box, box in enumerate(tops):
            box.v_order = i_box
        
        for i_col in range(1, cols_count):
            col = cols[i_col]
            for i_box, box in enumerate(col):
                weight = 0
                count  = 0
                for bx in cols[i_col-1]:
                    if bx in box.outputs:
                        weight += bx.v_order
                        count  += 1
                try:
                    box.v_order = weight / count
                except ZeroDivisionError as e:
                    print(f"Strange: the box {box} in col {i_col} doesn't have outputs: {box.outputs}")
                    print(f"Parent is: {box.parent}")
                    print(e)
                    Box.dump_links()
                    raise RuntimeError("STOP")
                
            col.sort(key=lambda b: b.v_order)
            
        # ----- Let's arrange in the boxes
        
        x = 0.
        for i_col, col in enumerate(cols):
            
            # ----- x backwards for the previous columun
            
            x -= cols_width[i_col] + self.H_MARGIN
            
            # ----- y at top with as a littls shift downwards
            
            y = -Box.V_STEP * i_col
                
            # ----- Loop on the boxes in the column

            for box in col:
                
                # ----- x and y location
                
                box.x = x + box.width
                ybox = y-30
                
                # ----- Can we move the box downwards to be closer to the linked boxed
                # in the previous column
                
                if i_col > 0:
                    prev = box.outputs[0]
                    ybox = min(ybox, prev.y)
                
                # ----- y for the next box
                
                box.y = ybox
                y = ybox - (box.height + self.V_MARGIN)
                
        self.update()
                
        if False:
            print('-'*30)
            print(f"Dump cols of {self}: count={cols_count}")
            for i, col in enumerate(cols):
                print(f"{i:2d}> {cols_width[i]:4.0f} {cols_height[i]:4.0f} : {col}")
                for box in col:
                    print(f"     ({box.x:4.0f}, {box.y:4.0f}) ({box.width:4.0f}, {box.height:4.0f})- {box}")
            print()
            
            
            
                
                
                
# ====================================================================================================
# A node box

class NodeBox(Box):
    def __init__(self, bnode):
        super().__init__()
        self.bnode = bnode
        self.name  = bnode.name
        
    def update(self):
        self.bnode.update()
        
    @property
    def x(self):
        return self.bnode.location.x
    
    @x.setter
    def x(self, value):
        self.bnode.location.x = value
    
    @property
    def y(self):
        return self.bnode.location.y
    
    @y.setter
    def y(self, value):
        self.bnode.location.y = value
        
    @property
    def width(self):
        if len(self):
            x0 = self[0].x
            x1 = x0 + self[0].width
            for box in self:
                x0 = min(x0, box.x)
                x1 = max(x1, box.x + box.width)
            return (x1 - x0) + 100
        else:
            return DIMS[type(self.bnode).__name__][0]/2
        
            
        return self.width_
        return self.bnode.dimensions[0]
    
    @property
    def height(self):
        if len(self):
            y0 = self[0].y
            y1 = y0 + self[0].height
            for box in self:
                y0 = min(y0, box.y)
                y1 = max(y1, box.y + box.height)
            return (y1 - y0) + 100
        else:
            return DIMS[type(self.bnode).__name__][1]/2
        
        return self.height_
        return self.bnode.dimensions[1]
    
        
# ====================================================================================================
# A tree box

class TreeBox(Box):
    
    def __init__(self, name):
        super().__init__()
        
        self.name   = name
        self.bnodes = bpy.data.node_groups[name].nodes
        self.blinks = bpy.data.node_groups[name].links
        
        # ---------------------------------------------------------------------------
        # First build the list of NodeBoxes
        
        boxes  = []
        for bnode in self.bnodes:
            boxes.append(NodeBox(bnode))
            
        def get_box(bnode):
            for box in boxes:
                if box.bnode == bnode:
                    return box
            return None

        # ---------------------------------------------------------------------------
        # Build the links
        
        for blink in self.blinks:
            box0 = get_box(blink.from_node)
            box1 = get_box(blink.to_node)
            Box.link(box0, box1)
            
        # ---------------------------------------------------------------------------
        # Place the boxes in their parent
        
        for box in boxes:
            if box.bnode.parent is None:
                self.append(box)
                box.parent = self
            else:
                frame = get_box(box.bnode.parent)
                frame.append(box)
                box.parent = frame

        # ---------------------------------------------------------------------------
        # Place the boxes in their parent
                
        self.update_frame_links()
        
        
    def update(self):
        self.bnodes.update()
        
# ====================================================================================================
# Arrange a tree

def arrange(name):
    tree = TreeBox(name)
    tree.arrange_children()
    
        
        
        
        
                
        