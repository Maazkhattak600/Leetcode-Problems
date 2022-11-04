class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        #Adjaceny list
        
        prereq = {c:[] for c in range(numCourses)}
        
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        #A course willl have three possible states 
        # Already visited == course has been added to the output
        #visiting - course has not been added to output and added to the cycle
        #Not visited at all : Course has not aaded to output or cycle
        
        output = []
        
        visit , cycle = set(), set()
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        
        return output
            