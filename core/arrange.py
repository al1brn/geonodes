#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 08:10:09 2022

@author: alain
"""

import bpy

DIMS = {
     'FunctionNodeAlignEulerToVector': (280.0, 468.0),
     'FunctionNodeBooleanMath': (280.0, 254.0),
     'FunctionNodeCompare': (280.0, 308.0),
     'FunctionNodeFloatToInt': (280.0, 210.0),
     'FunctionNodeInputBool': (280.0, 160.0),
     'FunctionNodeInputColor': (280.0, 370.0),
     'FunctionNodeInputInt': (280.0, 160.0),
     'FunctionNodeInputSpecialCharacters': (280.0, 144.0),
     'FunctionNodeInputString': (280.0, 160.0),
     'FunctionNodeInputVector': (280.0, 240.0),
     'FunctionNodeLegacyRandomFloat': (280.0, 238.0),
     'FunctionNodeRandomValue': (280.0, 346.0),
     'FunctionNodeReplaceString': (280.0, 238.0),
     'FunctionNodeRotateEuler': (280.0, 428.0),
     'FunctionNodeSliceString': (280.0, 238.0),
     'FunctionNodeStringLength': (280.0, 150.0),
     'FunctionNodeValueToString': (280.0, 194.0),
     'GeometryNodeAccumulateField': (280.0, 396.0),
     'GeometryNodeAttributeDomainSize': (280.0, 346.0),
     'GeometryNodeAttributeRemove': (280.0, 194.0),
     'GeometryNodeAttributeStatistic': (280.0, 664.0),
     'GeometryNodeAttributeTransfer': (280.0, 356.0),
     'GeometryNodeBoundBox': (280.0, 238.0),
     'GeometryNodeCaptureAttribute': (280.0, 356.0),
     'GeometryNodeCollectionInfo': (280.0, 298.0),
     'GeometryNodeConvexHull': (280.0, 150.0),
     'GeometryNodeCurveArc': (280.0, 434.0),
     'GeometryNodeCurveEndpointSelection': (280.0, 194.0),
     'GeometryNodeCurveHandleTypeSelection': (280.0, 210.0),
     'GeometryNodeCurveLength': (280.0, 150.0),
     'GeometryNodeCurvePrimitiveBezierSegment': (280.0, 866.0),
     'GeometryNodeCurvePrimitiveCircle': (280.0, 258.0),
     'GeometryNodeCurvePrimitiveLine': (280.0, 498.0),
     'GeometryNodeCurvePrimitiveQuadrilateral': (280.0, 258.0),
     'GeometryNodeCurveQuadraticBezier': (280.0, 642.0),
     'GeometryNodeCurveSetHandles': (280.0, 304.0),
     'GeometryNodeCurveSpiral': (280.0, 370.0),
     'GeometryNodeCurveSplineType': (280.0, 254.0),
     'GeometryNodeCurveStar': (280.0, 326.0),
     'GeometryNodeCurveToMesh': (280.0, 238.0),
     'GeometryNodeCurveToPoints': (280.0, 390.0),
     'GeometryNodeDeleteGeometry': (280.0, 304.0),
     'GeometryNodeDistributePointsOnFaces': (340.0, 430.0),
     'GeometryNodeDualMesh': (280.0, 194.0),
     'GeometryNodeExtrudeMesh': (280.0, 474.0),
     'GeometryNodeFieldAtIndex': (280.0, 312.0),
     'GeometryNodeFillCurve': (280.0, 210.0),
     'GeometryNodeFilletCurve': (280.0, 298.0),
     'GeometryNodeFlipFaces': (280.0, 194.0),
     'GeometryNodeGeometryToInstance': (320.0, 150.0),
     'GeometryNodeGroup': (280.0, 100.0),
     'GeometryNodeImageTexture': (480.0, 392.0),
     'GeometryNodeInputCurveHandlePositions': (300.0, 194.0),
     'GeometryNodeInputCurveTilt': (280.0, 100.0),
     'GeometryNodeInputID': (280.0, 100.0),
     'GeometryNodeInputIndex': (280.0, 100.0),
     'GeometryNodeInputMaterial': (280.0, 160.0),
     'GeometryNodeInputMaterialIndex': (280.0, 100.0),
     'GeometryNodeInputMeshEdgeAngle': (280.0, 144.0),
     'GeometryNodeInputMeshEdgeNeighbors': (280.0, 100.0),
     'GeometryNodeInputMeshEdgeVertices': (280.0, 232.0),
     'GeometryNodeInputMeshFaceArea': (280.0, 100.0),
     'GeometryNodeInputMeshFaceNeighbors': (300.0, 144.0),
     'GeometryNodeInputMeshIsland': (280.0, 144.0),
     'GeometryNodeInputMeshVertexNeighbors': (280.0, 144.0),
     'GeometryNodeInputNormal': (280.0, 100.0),
     'GeometryNodeInputPosition': (280.0, 100.0),
     'GeometryNodeInputRadius': (280.0, 100.0),
     'GeometryNodeInputSceneTime': (280.0, 144.0),
     'GeometryNodeInputShadeSmooth': (280.0, 100.0),
     'GeometryNodeInputSplineCyclic': (280.0, 100.0),
     'GeometryNodeInputSplineResolution': (280.0, 100.0),
     'GeometryNodeInputTangent': (280.0, 100.0),
     'GeometryNodeInstanceOnPoints': (280.0, 654.0),
     'GeometryNodeInstancesToPoints': (280.0, 282.0),
     'GeometryNodeIsViewport': (280.0, 100.0),
     'GeometryNodeJoinGeometry': (280.0, 150.0),
     'GeometryNodeLegacyAlignRotationToVector': (280.0, 562.0),
     'GeometryNodeLegacyAttributeClamp': (280.0, 440.0),
     'GeometryNodeLegacyAttributeColorRamp': (480.0, 468.0),
     'GeometryNodeLegacyAttributeCombineXYZ': (280.0, 474.0),
     'GeometryNodeLegacyAttributeCompare': (280.0, 442.0),
     'GeometryNodeLegacyAttributeConvert': (280.0, 348.0),
     'GeometryNodeLegacyAttributeCurveMap': (480.0, 678.0),
     'GeometryNodeLegacyAttributeFill': (280.0, 352.0),
     'GeometryNodeLegacyAttributeMapRange': (280.0, 568.0),
     'GeometryNodeLegacyAttributeMath': (280.0, 442.0),
     'GeometryNodeLegacyAttributeMix': (280.0, 524.0),
     'GeometryNodeLegacyAttributeProximity': (280.0, 342.0),
     'GeometryNodeLegacyAttributeRandomize': (280.0, 436.0),
     'GeometryNodeLegacyAttributeSampleTexture': (480.0, 282.0),
     'GeometryNodeLegacyAttributeSeparateXYZ': (280.0, 386.0),
     'GeometryNodeLegacyAttributeTransfer': (280.0, 392.0),
     'GeometryNodeLegacyAttributeVectorMath': (280.0, 442.0),
     'GeometryNodeLegacyAttributeVectorRotate': (330.0, 890.0),
     'GeometryNodeLegacyCurveEndpoints': (280.0, 194.0),
     'GeometryNodeLegacyCurveReverse': (280.0, 194.0),
     'GeometryNodeLegacyCurveSelectHandles': (280.0, 304.0),
     'GeometryNodeLegacyCurveSetHandles': (280.0, 304.0),
     'GeometryNodeLegacyCurveSplineType': (280.0, 254.0),
     'GeometryNodeLegacyCurveSubdivide': (280.0, 254.0),
     'GeometryNodeLegacyCurveToPoints': (280.0, 258.0),
     'GeometryNodeLegacyDeleteGeometry': (280.0, 238.0),
     'GeometryNodeLegacyEdgeSplit': (280.0, 282.0),
     'GeometryNodeLegacyMaterialAssign': (280.0, 238.0),
     'GeometryNodeLegacyMeshToCurve': (280.0, 194.0),
     'GeometryNodeLegacyPointDistribute': (280.0, 342.0),
     'GeometryNodeLegacyPointInstance': (280.0, 258.0),
     'GeometryNodeLegacyPointScale': (280.0, 378.0),
     'GeometryNodeLegacyPointSeparate': (280.0, 238.0),
     'GeometryNodeLegacyPointTranslate': (280.0, 374.0),
     'GeometryNodeLegacyPointsToVolume': (340.0, 392.0),
     'GeometryNodeLegacyRaycast': (480.0, 826.0),
     'GeometryNodeLegacyRotatePoints': (280.0, 474.0),
     'GeometryNodeLegacySelectByMaterial': (280.0, 238.0),
     'GeometryNodeLegacySubdivisionSurface': (300.0, 348.0),
     'GeometryNodeLegacyVolumeToMesh': (340.0, 342.0),
     'GeometryNodeMaterialSelection': (280.0, 150.0),
     'GeometryNodeMergeByDistance': (280.0, 238.0),
     'GeometryNodeMeshBoolean': (280.0, 342.0),
     'GeometryNodeMeshCircle': (280.0, 254.0),
     'GeometryNodeMeshCone': (280.0, 562.0),
     'GeometryNodeMeshCube': (280.0, 402.0),
     'GeometryNodeMeshCylinder': (280.0, 518.0),
     'GeometryNodeMeshGrid': (280.0, 282.0),
     'GeometryNodeMeshIcoSphere': (280.0, 194.0),
     'GeometryNodeMeshLine': (280.0, 538.0),
     'GeometryNodeMeshToCurve': (280.0, 194.0),
     'GeometryNodeMeshToPoints': (280.0, 342.0),
     'GeometryNodeMeshUVSphere': (280.0, 238.0),
     'GeometryNodeObjectInfo': (280.0, 386.0),
     'GeometryNodePointsToVertices': (280.0, 194.0),
     'GeometryNodePointsToVolume': (340.0, 342.0),
     'GeometryNodeProximity': (280.0, 298.0),
     'GeometryNodeRaycast': (300.0, 736.0),
     'GeometryNodeRealizeInstances': (280.0, 150.0),
     'GeometryNodeReplaceMaterial': (280.0, 238.0),
     'GeometryNodeResampleCurve': (280.0, 302.0),
     'GeometryNodeReverseCurve': (280.0, 194.0),
     'GeometryNodeRotateInstances': (280.0, 566.0),
     'GeometryNodeSampleCurve': (280.0, 342.0),
     'GeometryNodeScaleElements': (280.0, 396.0),
     'GeometryNodeScaleInstances': (280.0, 566.0),
     'GeometryNodeSeparateComponents': (280.0, 326.0),
     'GeometryNodeSeparateGeometry': (280.0, 298.0),
     'GeometryNodeSetCurveHandlePositions': (280.0, 462.0),
     'GeometryNodeSetCurveRadius': (280.0, 238.0),
     'GeometryNodeSetCurveTilt': (280.0, 238.0),
     'GeometryNodeSetID': (280.0, 238.0),
     'GeometryNodeSetMaterial': (280.0, 238.0),
     'GeometryNodeSetMaterialIndex': (280.0, 238.0),
     'GeometryNodeSetPointRadius': (280.0, 238.0),
     'GeometryNodeSetPosition': (280.0, 402.0),
     'GeometryNodeSetShadeSmooth': (280.0, 238.0),
     'GeometryNodeSetSplineCyclic': (280.0, 238.0),
     'GeometryNodeSetSplineResolution': (280.0, 238.0),
     'GeometryNodeSplineLength': (280.0, 144.0),
     'GeometryNodeSplineParameter': (280.0, 188.0),
     'GeometryNodeSplitEdges': (280.0, 194.0),
     'GeometryNodeStringJoin': (280.0, 194.0),
     'GeometryNodeStringToCurves': (380.0, 722.0),
     'GeometryNodeSubdivideCurve': (280.0, 194.0),
     'GeometryNodeSubdivideMesh': (280.0, 194.0),
     'GeometryNodeSubdivisionSurface': (300.0, 348.0),
     'GeometryNodeSwitch': (280.0, 306.0),
     'GeometryNodeTransform': (280.0, 642.0),
     'GeometryNodeTranslateInstances': (280.0, 402.0),
     'GeometryNodeTriangulate': (280.0, 348.0),
     'GeometryNodeTrimCurve': (280.0, 302.0),
     'GeometryNodeViewer': (280.0, 148.0),
     'GeometryNodeVolumeToMesh': (340.0, 298.0),
     'NodeFrame': (300.0, 200.0),
     'NodeGroupInput': (280.0, 144.0),
     'NodeGroupOutput': (280.0, 144.0),
     'NodeReroute': (16.0, 16.0),
     'ShaderNodeClamp': (280.0, 298.0),
     'ShaderNodeCombineRGB': (280.0, 238.0),
     'ShaderNodeCombineXYZ': (280.0, 238.0),
     'ShaderNodeFloatCurve': (480.0, 584.0),
     'ShaderNodeMapRange': (280.0, 494.0),
     'ShaderNodeMath': (280.0, 308.0),
     'ShaderNodeMixRGB': (280.0, 342.0),
     'ShaderNodeRGBCurve': (480.0, 584.0),
     'ShaderNodeSeparateRGB': (280.0, 238.0),
     'ShaderNodeSeparateXYZ': (280.0, 358.0),
     'ShaderNodeTexBrick': (300.0, 780.0),
     'ShaderNodeTexChecker': (280.0, 326.0),
     'ShaderNodeTexGradient': (280.0, 254.0),
     'ShaderNodeTexMagic': (280.0, 342.0),
     'ShaderNodeTexMusgrave': (300.0, 440.0),
     'ShaderNodeTexNoise': (280.0, 430.0),
     'ShaderNodeTexVoronoi': (280.0, 490.0),
     'ShaderNodeTexWave': (300.0, 618.0),
     'ShaderNodeTexWhiteNoise': (280.0, 258.0),
     'ShaderNodeValToRGB': (480.0, 424.0),
     'ShaderNodeValue': (280.0, 160.0),
     'ShaderNodeVectorCurve': (480.0, 704.0),
     'ShaderNodeVectorMath': (280.0, 502.0),
     'ShaderNodeVectorRotate': (280.0, 636.0)
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
    
        
        
        
        
                
        