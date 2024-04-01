class Node:
    def __init__(self,song_id):
        self.song_id = song_id
        self.next = None

class EmptyListException:
    def __init__(self,message):
        super().__init__(message)

class PlayList:
    def __init__(self):
        self.head = None
    
    def __len__(self):
        count =0
        current = self.head
        while current:
            count +=1
            current = current.next
        return count
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.song_id
            current = current.next

    def add_song (self,song_id):
        new_node = Node(song_id)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_playlist(self):
        current = self.head
        while current:
            print(current.song_id,end=" -->")
            current = current.next
        print("None")
    
    def reverse_playlist(self):

        prev =None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current =next_node
        self.head = prev
    
    def pop(self):
        if self.head is None:
            raise EmptyListException("Cannot pop from an empty list")
        song_id = self.head.song_id
        self.head = self.head.next
        return song_id
    
