class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()
        j=0
        count=0
        for i in range(min(len(players),len(trainers))):
            while j<len(trainers) and trainers[j]<players[i]:
                j+=1
            if j>=len(trainers):
                return count
            count+=1
            j+=1
        return count
