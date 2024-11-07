import threading
from concurrent import futures
from time import sleep

import grpc
from grpc_health.v1 import health, health_pb2, health_pb2_grpc


class HealthServer(object):

    def __init__(self, server: grpc.Server, service: str = "health", max_workers: int = 10, sleep_time: int = 5):
        self.server = server
        self.service = service
        self.max_workers = max_workers
        self.sleep_time = sleep_time

    def _toggle_health(self, health_servicer: health.HealthServicer):
        next_status = health_pb2.HealthCheckResponse.SERVING
        while True:
            if next_status == health_pb2.HealthCheckResponse.SERVING:
                next_status = health_pb2.HealthCheckResponse.NOT_SERVING
            else:
                next_status = health_pb2.HealthCheckResponse.SERVING

            health_servicer.set(self.service, next_status)
            sleep(self.sleep_time)

    def configure_health_server(self):
        health_servicer = health.HealthServicer(
            experimental_non_blocking=True,
            experimental_thread_pool=futures.ThreadPoolExecutor(max_workers=self.max_workers),
        )
        health_pb2_grpc.add_HealthServicer_to_server(health_servicer, self.server)

        # Use a daemon thread to toggle health status
        toggle_health_status_thread = threading.Thread(target=self._toggle_health, args=(health_servicer,), daemon=True)
        toggle_health_status_thread.start()
