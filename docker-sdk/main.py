#!/usr/bin/python3

import docker
from docker.errors import APIError, BuildError
from Sandbox import Sandbox
from Monitor import Monitor
from NetworkMonitor import NetworkMonitor
from ProcessMonitor import ProcessMonitor
from PerformanceMonitor import PerformanceMonitor


def getMonitorsToLoad() -> list[Monitor]:
    # Add new Modules here
    toLoad = []
    toLoad.append(NetworkMonitor())
    toLoad.append(PerformanceMonitor())
    toLoad.append(ProcessMonitor())
    return toLoad


def buildImage(image_client) -> tuple[object, object]:
    try:
        return image_client.build(path="./sandbox/", tag="secureharbor:0.1", nocache=True, rm=True)
    except APIError as err:
        print(err)
    except BuildError as err:
        print(err)
    except TypeError as err:
        print(err)


def main():
    # Docker SDK Setup
    docker_client = docker.from_env()
    container_client = docker_client.containers
    image_client = docker_client.images

    # Generate Docker Image
    image_generation_output = buildImage(image_client)
    if image_generation_output is None:
        exit(1)
    image = image_generation_output[0]

    # Run Container & load Modules
    container = container_client.run(image=image, runtime="runsc", detach=True)
    monitors = getMonitorsToLoad()
    sandbox = Sandbox(container=container, monitors=monitors)
    sandbox.runMonitors()

    # Stop Container
    sandbox.terminate()


if __name__ == "__main__":
    main()
