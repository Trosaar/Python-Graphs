import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i}")
        # Create Frienships
        # Generate all possible friendship combinations
        possible_friendships = []
        # Avoid duplicates by ensuring the first number is smaller than the second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        # Shuffle the possible friendships
        random.shuffle(possible_friendships)
        # Create friendships for the first X pairs of the list
        # X is determined by the formula: num_users * avg_friendships // 2
        # Need to divide by 2 since each add_friendship() creates 2 friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        '''
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        for person in self.users:
            visited_connection = set()
            path = []
            path.append([user_id])
            
            while len(path) > 0:
                connection_check = path.pop(0)

                if connection_check[-1] is person:
                    visited[person] = connection_check
                    visited_connection.add(connection_check[-1])

                if connection_check[-1] not  in visited_connection:
                    visited_connection.add(connection_check[-1])

                    for connection in self.friendships[connection_check[-1]]:
                        updated_path = list(connection_check)
                        updated_path = connection_check + [connection]
                        path.append(updated_path)        
        
        return visited
        '''

        # want to refactor Artem's code to not use Queue
        neighbors_to_visit = Queue()
        visited = {}
        neighbors_to_visit.enqueue( [ user_id ])
        while neighbors_to_visit.size() > 0:
            # dequeue the first path
            current_path = neighbors_to_visit.dequeue()
            # Grab the last vertex 
            current_vertex = current_path[-1]
            # if it has not been visited
            if current_vertex not in visited:
                # when we reach the unvisited vertex, add it to visited dict
                # but also, add the whole path that lead us here
                visited[current_vertex] = current_path
                # get all neighbors and add the path + the neighbor to the queue
                for neighbor in self.friendships[current_vertex]:
                    path_copy = current_path.copy()
                    path_copy.append(neighbor)
                    neighbors_to_visit.enqueue(path_copy)

        # !!!! IMPLEMENT ME
        return visited



if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
