import pyrealsense2 as rs


def saveply():
    point_cloud = rs.pointcloud()
    points = rs.points()
    pipe = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.depth)
    pipe.start(config)
    colorizer = rs.colorizer()

    try:
        frames = pipe.wait_for_frames()
        colorized = colorizer.process(frames)
        ply = rs.save_to_ply("saved.ply")
        ply.set_option(rs.save_to_ply.option_ply_binary, True)
        ply.set_option(rs.save_to_ply.option_ply_normals, True)
        ply.process(colorized)
        print("Done")
    finally:
        pipe.stop()


if __name__ == "__main__":
    saveply()