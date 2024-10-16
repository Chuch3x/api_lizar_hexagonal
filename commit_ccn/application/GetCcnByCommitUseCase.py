from typing import List
from ..domain.CommitMetricsRepository import CommitMetricsRepository
from ..domain.CommitMetrics import CommitMetrics

class GetCcnByCommitUseCase:
    def __init__(self, repository: 'CommitMetricsRepository'):
        self.repository = repository

    def run(self) -> List['CommitMetrics']:
        return self.repository.get_ccn_by_commit()
