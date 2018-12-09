colors = ['Red', 'Green', 'Blue', 'Yellow', 'Black', ]

districts = ['Bilaspur', 'Chamba', 'Hamirpur', 'Kangra', 'Kinnaur', 'Kullu',
             'Lahaul & Spiti','Mandi', 'Shimla', 'Sirmaur', 'Solan', 'Una']

neighbors = {}
neighbors['Bilaspur'] = ['Una', 'Hamirpur', 'Mandi', 'Solan']
neighbors['Chamba'] = ['Lahaul & Spiti', 'Kangra']
neighbors['Hamirpur'] = ['Kangra', 'Mandi', 'Bilaspur', 'Una']
neighbors['Kangra'] = ['Chamba', 'Lahaul & Spiti', 'Kullu', 'Mandi', 'Hamirpur', 'Una']
neighbors['Kinnaur'] = ['Lahaul & Spiti', 'Shimla', 'Kullu']
neighbors['Kullu'] = ['Lahaul & Spiti', 'Kinnaur', 'Shimla', 'Mandi', 'Kangra']
neighbors['Lahaul & Spiti'] = ['Kinnaur', 'Kullu', 'Kangra', 'Chamba']
neighbors['Mandi'] = ['Kangra', 'Kullu', 'Shimla', 'Solan', 'Bilaspur', 'Hamirpur']
neighbors['Shimla'] = ['Kullu', 'Kinnaur', 'Sirmaur', 'Solan', 'Mandi']
neighbors['Sirmaur'] = ['Shimla', 'Solan']
neighbors['Solan'] = ['Mandi', 'Shimla', 'Sirmaur', 'Bilaspur']
neighbors['Una'] = ['Kangra', 'Hamirpur', 'Bilaspur']

colors_of_districts = {}

def promising(district, color):
    for neighbor in neighbors.get(district):
        color_of_neighbor = colors_of_districts.get(neighbor)
        if color_of_neighbor == color:
            return False
    return True


def get_color_for_district(district):
    for color in colors:
        if promising(district, color):
            return color

def main():
    for district in districts:
        colors_of_districts[district] = get_color_for_district(district)

    for color_dis in colors_of_districts:
        print(color_dis+": "+ colors_of_districts[color_dis])

main()