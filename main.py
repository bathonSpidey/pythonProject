# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pyrealsense2 as rs


def start():
# Create a context object. This object owns the handles to all connected realsense devices
    pipeline = rs.pipeline()
    pipeline.start()

    try:
        while True:
            # Create a pipeline object. This object configures the streaming camera and owns it's handle
            frames = pipeline.wait_for_frames()
            depth = frames.get_depth_frame()
            if not depth: continue

            # Print a simple text-based representation of the image, by breaking it into 10x20 pixel regions and approximating the coverage of pixels within one meter
            coverage = [0]*64
            for y in range(480):
                for x in range(640):
                    dist = depth.get_distance(x, y)
                    if 0 < dist and dist < 1:
                        coverage[int(x/10)] += 1

                if y%20 == 19:
                    line = ""
                    for c in coverage:
                        line += " .:nhBXWW"[int(c/25)]
                    coverage = [0]*64
                    print(line)

    finally:
        pipeline.stop()
if __name__ == '__main__':
    start()

