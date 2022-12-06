import pyrealsense2 as rs
import numpy as np


def savePly():
    point_cloud = rs.pointcloud()
    points = rs.points()
    pipe = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.depth)
    pipe.start(config)
    colorizer = rs.colorizer()
    print(points)

    try:
        frames = pipe.wait_for_frames()
        aligned_depth_frame = frames.get_depth_frame()
        points = point_cloud.calculate(aligned_depth_frame)
        print(points)
        vertices = np.asanyarray(points.get_vertices(dims=2))
        print(vertices)
        np.savetxt("test.txt", vertices)
        colorized = colorizer.process(frames)
        ply = rs.save_to_ply("saved.ply")
        ply.set_option(rs.save_to_ply.option_ply_binary, True)
        ply.set_option(rs.save_to_ply.option_ply_normals, True)
        processed = ply.process(colorized)
        print("Done")
    finally:
        pipe.stop()


if __name__ == "__main__":
    savePly()
