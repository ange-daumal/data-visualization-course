import os

from dotenv import load_dotenv
from py2neo import Graph

load_dotenv(".env")


class GraphDriver(object):

    @classmethod
    def from_env(cls, prefix="NEO4J"):
        uri: str = os.getenv(f"{prefix}_URI")
        usr: str = os.getenv(f"{prefix}_USR")
        pwd: str = os.getenv(f"{prefix}_PWD")
        return cls(uri, usr, pwd)

    def __init__(self: object, uri: str, usr: str, pwd: str, test=True) -> None:
        self.graph: Graph = Graph(uri, auth=(usr, pwd))
        if test:
            self.graph.evaluate("MATCH (n) RETURN n LIMIT 1")

    def get_graph(self):
        return self.graph

    def run_query(self, query, **kwargs):
        return self.graph.run(query, kwargs)


if __name__ == "__main__":
    driver = GraphDriver.from_env()
