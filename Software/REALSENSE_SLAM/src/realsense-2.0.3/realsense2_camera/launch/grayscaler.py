Panels:
  - Class: rviz/Displays
    Help Height: 78
    Name: Displays
    Property Tree Widget:
      Expanded: ~
      Splitter Ratio: 0.5
    Tree Height: 158
  - Class: rviz/Selection
    Name: Selection
  - Class: rviz/Tool Properties
    Expanded:
      - /2D Pose Estimate1
      - /2D Nav Goal1
      - /Publish Point1
    Name: Tool Properties
    Splitter Ratio: 0.588679016
  - Class: rviz/Views
    Expanded:
      - /Current View1
    Name: Views
    Splitter Ratio: 0.5
  - Class: rviz/Time
    Experimental: false
    Name: Time
    SyncMode: 0
    SyncSource: Image
Visualization Manager:
  Class: ""
  Displays:
    - Alpha: 0.5
      Cell Size: 1
      Class: rviz/Grid
      Color: 160; 160; 164
      Enabled: true
      Line Style:
        Line Width: 0.0299999993
        Value: Lines
      Name: Grid
      Normal Cell Count: 0
      Offset:
        X: 0
        Y: 0
        Z: 0
      Plane: XY
      Plane Cell Count: 10
      Reference Frame: <Fixed Frame>
      Value: true
    - Alpha: 1
      Autocompute Intensity Bounds: true
      Autocompute Value Bounds:
        Max Value: 10
        Min Value: -10
        Value: true
      Axis: Z
      Channel Name: intensity
      Class: rviz/PointCloud2
      Color: 255; 255; 255
      Color Transformer: RGB8
      Decay Time: 0
      Enabled: true
      Invert Rainbow: false
      Max Color: 255; 255; 255
      Max Intensity: 4096
      Min Color: 0; 0; 0
      Min Intensity: 0
      Name: PointCloud2
      Position Transformer: XYZ
      Queue Size: 10
      Selectable: true
      Size (Pixels): 3
      Size (m): 0.00999999978
      Style: Flat Squares
      Topic: /camera/depth_registered/points
      Unreliable: false
      Use Fixed Frame: true
      Use rainbow: true
      Value: true
    - Class: rviz/Image
      Enabled: true
      Image Topic: /camera/color/image_rect_color
      Max Value: 1
      Median window: 5
      Min Value: 0
      Name: Image
      Normalize Range: true
      Queue Size: 2
      Transport Hint: raw
      Unreliable: false
      Value: true
    - Class: rviz/Image
      Enabled: true
      Image Topic: /camera/infra2/image_rect_raw
      Max Value: 1
      Median window: 5
      Min Value: 0
      Name: Image
      Normalize Range: true
      Queue Size: 2
      Transport Hint: raw
      Unreliable: false
      Value: true
    - Class: rviz/Image
      Enabled: true
      Image Topic: /camera/aligned_depth_to_color/image_raw
      Max Value: 1
      Median window: 5
      Min Value: 0
      Name: Image
      Normalize Range: true
      Queue Size: 2
      Transport Hint: raw
      Unreliable: false
      Value: true
    - Class: rviz/TF
      Enabled: true
      Frame Timeout: 15
      Frames:
        All Enabled: true
        camera_aligned_depth_to_color_frame:
          Value: true
        camera_aligned_depth_to_infra1_frame:
          Value: true
        camera_aligned_depth_to_infra2_frame:
          Value: true
        camera_color_frame:
          Value: true
        camera_color_optical_frame:
          Value: true
        camera_depth_frame:
          Value: true
        camera_depth_optical_frame:
          Value: true
        camera_infra1_frame:
          Value: true
        camera_infra1_optical_frame:
          Value: true
        camera_infra2_frame:
          Value: true
        camera_infra2_optical_frame:
          Value: true
        camera_link:
          Value: true
      Marker Scale: 1
      Name: TF
      Show Arrows: true
      Show Axes: true
      Show Names: true
      Tree:
        camera_link:
          camera_aligned_depth_to_color_frame:
            camera_color_optical_frame:
              {}
          camera_aligned_depth_to_infra1_frame:
            camera_infra1_optical_frame:
              {}
          camera_aligned_depth_to_infra2_frame:
            camera_infra2_optical_frame:
              {}
          camera_color_frame:
            {}
          camera_depth_frame:
            camera_depth_optical_frame:
              {}
          camera_infra1_frame:
            {}
          camera_infra2_frame:
            {}
      Update Interval: 0
      Value: true
  Enabled: true
  Global Options:
    Background Color: 48; 48; 48
    Default Light: true
    Fixed Frame: camera_link
    Frame Rate: 30
  Name: root
  Tools:
    - Class: rviz/Interact
      Hide Inactive Objects: true
    - Class: rviz/MoveCamera
    - Class: rviz/Select
    - Class: rviz/FocusCamera
    - Class: rviz/Measure
    - Class: rviz/SetInitialPose
      Topic: /initialpose
    - Class: rviz/SetGoal
      Topic: /move_base_simple/goal
    - Class: rviz/PublishPoint
      Single click: true
      Topic: /clicked_point
  Value: true
  Views:
    Current:
      Class: rviz/Orbit
      Distance: 4.49856806
      Enable Stereo Rendering:
        Stereo Eye Separation: 0.0599999987
        Stereo Focal Distance: 1
        Swap Stereo Eyes: false
        Value: false
      Focal Point:
        X: 1.49125516
        Y: -0.429086566
        Z: -0.414452523
      Focal Shape Fixed Size: true
      Focal Shape Size: 0.0500000007
      Invert Z Axis: false
      Name: Current View
      Near Clip Distance: 0.00999999978
      Pitch: 0.32039851
      Target Frame: <Fixed Frame>
      Value: Orbit (rviz)
      Yaw: 2.96858835
    Saved: ~
Window Geometry:
  Displays:
    collapsed: false
  Height: 1029
  Hide Left Dock: false
  Hide Right Dock: false
  Image:
    collapsed: false
  QMainWindow State: 000000ff00000000fd00000004000000000000016a0000037bfc020000000bfb0000001200530065006c0065006300740069006f006e00000001e10000009b0000006100fffffffb0000001e0054006f006f006c002000500072006f007000650072007400690065007302000001ed000001df00000185000000a3fb000000120056006900650077007300200054006f006f02000001df000002110000018500000122fb000000200054006f006f006c002000500072006f0070006500720074006900650073003203000002880000011d000002210000017afb000000100044006900730070006c00610079007301000000280000012d000000d700fffffffb0000002000730065006c0065006300740069006f006e00200062007500660066006500720200000138000000aa0000023a00000294fb00000014005700690064006500530074006500720065006f02000000e6000000d2000003ee0000030bfb0000000c004b0069006e0065006300740200000186000001060000030c00000261fb0000000a0049006d006100670065010000015b000000b50000001600fffffffb0000000a0049006d0061006700650100000216000000bf0000001600fffffffb0000000a0049006d00610067006501000002db000000c80000001600ffffff000000010000010f0000037bfc0200000003fb0000001e0054006f006f006c002000500072006f00700065007200740069006500730100000041000000780000000000000000fc000000280000037b000000ad00fffffffa000000010100000002fb0000000a0049006d0061006700650000000000ffffffff0000000000000000fb0000000a0056006900650077007301000003a10000010f0000010f00fffffffb0000001200530065006c0065006300740069006f006e010000025a000000b200000000000000000000000200000490000000a9fc0100000001fb0000000a00560069006500770073030000004e00000080000002e10000019700000003000004b00000003efc0100000002fb0000000800540069006d00650100000000000004b00000030000fffffffb0000000800540069006d006501000000000000045000000000000000000000022b0000037b00000004000000040000000800000008fc0000000100000002000000010000000a0054006f006f006c00730100000000ffffffff0000000000000000
  Selection:
    collapsed: false
  Time:
    collapsed: false
  Tool Properties:
    collapsed: false
  Views:
    collapsed: false
  Width: 1200
  X: 2448
  Y: 143

