from app.repository.SimianRepository import SimianRepository


class StatsService(object):

    @staticmethod
    def stats():
        return SimianRepository.get_stats()
