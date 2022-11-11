from pprint import pprint

def parse_input():
   map_height,map_width = [int(x) for x in (input()).split(' ')]
   map = []
   line = 0
   while line < map_height:
      map.append(input())
      line = line + 1
   
   num_moves = int(input())
   x1,y1,x2,y2 = [int(x) for x in (input()).split(' ')]
   
   pprint(map)
   

if __name__ == "__main__":
   parse_input()
