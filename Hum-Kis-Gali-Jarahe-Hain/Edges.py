from main import addEdges,addNodes, tocap


edges = [('Gate 2','MPR outer', 54, 170),
('MPR outer','Reception desk', 27, 200),
('Reception desk','Reception stairs',15,210),
('Reception stairs ground','Student Centre' ,15, 290),
('Reception desk','Reception Elevator ground',26,270),
('Reception desk', 'OCS', 30,280),
('Student Centre','Reception washroom' ,16,180),
('Reception desk','Turnstile',14,175),
('Turnstile','MPR inner',16,80),
('Turnstile','Library junction',40,178),
('Library junction','Student life office', 19,310),
('Student life office', 'Health and Wellness',40,310),
('Library junction', 'Cafe2go', 37,90),
('Library junction', 'Library', 33,62),
('Cafe2go','Cassim lab',36,185),
('Cassim lab', 'East level 1 faculty pods', 13,175),
('East level 1 faculty pods', 'Easten ramp ground', 29,206),
('Library junction', 'Central street ground faculty pods',43,207),
('Central street ground faculty pods','Central street stairs ground', 42,207),
('Central street ground faculty pods', 'ATM', 34,170),
('Central street ground faculty pods', 'Arif Habib classroom', 43,228),
('Arif Habib classroom', 'Earth courtyard',13,2),
('Earth courtyard', 'Westerm stairs ground' ,24,27),
('Western stairs ground', 'Physics lab' , 20,291),
('Physics lab', 'Western elevator ground', 8,290),
('Western elevator Ground', 'Math lab', 8,190),
('Physics lab', 'Earth boards', 20,200),
('Earth boards', 'Air courtyard' ,20,200),
('Air courtyard', 'Arif Habib classroom', 22,80),
('Air courtyard', 'Water courtyard',17,170),
('Water courtyard', 'Fire courtyard' ,37,200),
('Fire courtyard', 'Chemistry lab',20,255),
('Fire courtyard', 'Ecology lab'  ,20,255),
('Digital systems lab', 'Fire courtyard',24,130),
('Communications lab', 'Fire courtyard',24,130),
('Fire courtyard', 'Student lounge amphi end' ,55,150),
('Student lounge amphi end', 'Soorty hall',47,70),
('ATM stairs', 'Soorty hall' ,43,170),
('Soorty hall','Student lounge garden end',38,211),
('Student lounge garden end' ,'Courts Faculty pods',20,180),
('Courts Faculty pods', 'Courts' ,56,180),
('Courts', 'Zen garden' ,100,175),
('Courts', 'Rahim bhai stall' ,80,30),
('Rahim Bhai stall', 'Dhaba' ,24,108),
('Rahim Bhai stall', 'Dukaan' ,17,0),
('Dukaan', 'Tapal 1',11,90),
('Dukaan', 'Amphi washroom' ,23,330),
('Amphi washroom' , 'Amphi lower' ,15,260),
('Amphi lower', 'Amphi upper' ,40,180),
('Amphi upper', 'C-015' ,33,107,'s'),
('C-015', 'Gym' ,27,220),
('C-015', 'Swimming Pool',44,260),
('Swimming Pool', 'Facilities office',58,15),
('Facilities office', 'Changing room',44,96),
('Facilities office', 'Engineering workshop',21,53),
('Facilities office', 'Western Elevator lower ground',65,355),
('C-015', 'Dukaan',27,45),
('Tapal 1', 'Tapal 2',35,12),
('Tapal 2', 'Projects lab',25,2),
('Projects lab', 'Power lab',25,19),
('Power lab', 'Circuits lab',27,11),
('Circuits lab', 'Music room',23,100),
('Music room', 'Linux lab',7,90),
('Linux lab','Lower ground eastern washrooms',11,155),
('Lower ground eastern washrooms', 'Graphics lab',28,185),
('Graphics lab', 'Dinshaw', 10,180),
('Dinshaw', 'rangoonwala', 6,180),
('Dinshaw', 'Easter ramp lower',15,230),
('Eastern ramp lower', 'projects lab',31,290),
('Reception Elevator ground','Reception Elevator first',0,0),
('Reception Elevator first','Reception Elevator second',0,0),
('Reception Elevator second','Reception Elevator third',0,0),
('Western Elevator lower ground','Western Elevator ground',0,0),
('Western Elevator ground','Western Elevator first',0,0),
('Eastern ramp lower','Eastern ramp ground',84,0),
('Turnstile stairs ground','Turnstile',20,350),
('Turnstile stairs lower','Turnstile stairs ground',31,350),
('Turnstile stairs lower','Female lounge',52,277),
('Female lounge','Westerm stairs ground',30,175),
('Western pathway Air junction','Western pathway Wellness junction',59,4),
('Western pathway Wellness junction','Bank',81,9),
('Bank','Security office',20,18),
('Gate 2','Security office',70,280),
('ATM stairs','Tapal stairs',45,187),
('Tapal stairs','Dukaan',13,177),
('Tapal stairs','Amphi washroom',10,285),
('ATM','ATM stairs',13,190),
('Wellness courtyard','Western pathway Wellness junction',47,285),
('Student life office','Wellness courtyard',16,285),
('Central stairs ground','Central stairs first',24,33),
#######ASAD#########

('Film Studio', 'Tariq Rafi', 38, 260),
('Central street stairs top', 'Tariq Rafi', 24, 90),
('Central street stairs top', 'W221 Faculty Pod', 49, 302),
('W221 Faculty Pod', 'W242', 30, 160),
('W221 Faculty Pod', 'W243', 47, 174),
('W242', 'W243', 17, 200),
('W242', 'W244 Design Lab', 19, 60),
('W221 Faculty Pod', 'Western Elevator first', 12, 40),
('Western Elevator first', 'C203 Faculty Pod', 36, 140),
('C203 Faculty Pod', 'CPE C201', 51, 32),
('CPE C201', 'Library Entrance 1st Floor', 35, 100),
('CPE C201', 'CPE Classroom', 54,0),  # Audi Route
('CPE C201', 'CPE Classroom', 42,0),  # Deans Pod Route
('Library Entrance 1st Floor', 'Discussion Rooms', 34, 140),
('Library Entrance 1st Floor',  'Yohsin Hall', 40, 64),
('CPE Classroom', 'Deans Pod', 44, 300),
('CPE Classroom', 'Auditorium', 30, 80),
('CPE Classroom', 'Reception Elevator first', 12, 340),
('CPE Classroom', 'Faculty Pods', 19, 217),
('CPE Classroom', 'Standard Chartered Classroom', 28,317),
('CPE Classroom', 'N219 Pods', 32, 350),
('Reception Staris first', 'CPE C201', 26, 226),
('Reception Stairs first', 'Auditorium', 31, 200),
('Reception Stairs first', 'CPE Classroom', 30, 330),
('Reception Stairs second', 'Playground',5, 55),
('Playground' , 'Marcom', 35, 330),
('Marcom', 'Reception Elevator second', 7,7)




]
edges1 = [('Gate 2','MPR outer', 54, 170),
('MPR outer','Reception desk', 27, 200),
('Reception desk','Reception stairs ground',15,210),
('Reception stairs ground','Student Centre' ,15, 290),
('Reception desk','Reception Elevator ground',26,270),
('Reception desk', 'OCS', 30,280),
('Student Centre','Reception washroom' ,16,180),
('Reception desk','Turnstile',14,175),
('Turnstile','MPR inner',16,80),
('Turnstile','Library junction',40,178),
('Library junction','Student life office', 19,310),
('Student life office', 'Health and Wellness',40,310),
('Library junction', 'Cafe2go', 37,90),
('Library junction', 'Library', 33,62),
('Cafe2go','Cassim lab',36,185),
('Cassim lab', 'East level 1 faculty pods', 13,175),
('East level 1 faculty pods', 'Easten ramp ground', 29,206),
('Library junction', 'Central street ground faculty pods',43,207),
('Central street ground faculty pods','Central street stairs ground', 42,207),
('Central street ground faculty pods', 'ATM', 34,170),
('Central street ground faculty pods', 'Arif Habib classroom', 43,228),
('Arif Habib classroom', 'Earth courtyard',13,2),
('Earth courtyard', 'Westerm stairs ground' ,24,27),
('Western stairs ground', 'Physics lab' , 20,291),
('Physics lab', 'Western elevator ground', 8,290),
#add
('Physics lab', 'Math lab', 4,290),
('Western elevator Ground', 'Math lab', 8,190),
('Physics lab', 'Earth boards', 20,200),
('Earth boards', 'Air courtyard' ,20,200),
('Air courtyard', 'Arif Habib classroom', 22,80),
('Air courtyard', 'Water courtyard',17,170),
('Water courtyard', 'Fire courtyard' ,37,200),
('Fire courtyard', 'Chemistry lab',20,255),
('Fire courtyard', 'Ecology lab'  ,20,255),
('Digital systems lab', 'Fire courtyard',24,130),
('Communications lab', 'Fire courtyard',24,130),
('Fire courtyard', 'Student lounge amphi end' ,55,150),
('Student lounge amphi end', 'Soorty hall',47,70),
('ATM', 'Soorty hall' ,55,170),
('Soorty hall','Student lounge garden end',38,211),
('Student lounge garden end' ,'Courts Faculty pods',20,180),
('Courts Faculty pods', 'Courts' ,56,180),
('Courts', 'Zen garden',100,175)
#######ASAD#########
]
Edges = []
def out(edges,Edges):
    for i in edges:
        Edges.append(i)
        if len(i)==4:
            x = (i[1],i[0],i[2],(180 - i[3]))
        else:
            x = (i[1],i[0],i[2],(180 - i[3]))
        Edges.insert(Edges.index(i),x)
    return Edges

Edges = out(edges,Edges)
# print(Edges)
G=addNodes(Edges,[])
addEdges(G,Edges)
positions1=[]

mapposition=edges1[:]
p=[(5, 350), (142, 311), (215, 345), (249, 344), (237, 387), (204, 419), (154, 390), (295, 365), (248, 321),
 (216, 306), (362, 284), (368, 361), (335, 590), (332, 199), (290, 221), (443, 152), (530, 146), (618, 181), (522, 361), (623, 284), (640, 411), (596, 413), (564, 436), (475, 470), (489, 496), (513, 487), (540, 474), (587, 495), (627, 465), (662, 490), (693, 480), (693, 497), (638, 499), (635, 474), (798, 384), (737, 281), (852, 322), (902, 344), (965, 303), (1175, 228)]
a=0
while len(p)>0 and len(mapposition)>a:
    if a==0:
        positions1.append((mapposition[a][0],p[0]))
        p.pop(0)
        a+=1
        continue
    if mapposition[a][0] not in [i[0] for i in positions1]:
        positions1.append((mapposition[a][0],p[0]))
        p.pop(0)
    if mapposition[a][1] not in [i[0] for i in positions1]:
        positions1.append((mapposition[a][1],p[0]))
        p.pop(0)
        mapposition.pop(0)
    a+=1
# print ('\n'*5,positions1)
# print('\n'*5,edges1)
# positions1=tocap(positions1)
# print('Here\n'*5,positions1)

G1=addNodes(edges1,[])
addEdges(G1,edges1)


