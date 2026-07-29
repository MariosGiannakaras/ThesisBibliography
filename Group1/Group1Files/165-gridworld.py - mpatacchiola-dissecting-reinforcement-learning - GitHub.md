> Source: https://github.com/mpatacchiola/dissecting-reinforcement-learning/blob/master/environments/gridworld.py

dissecting-reinforcement-learning/environments/gridworld.py at master · mpatacchiola/dissecting-reinforcement-learning · GitHub
Skip to content
Navigation Menu
Toggle navigation 
Sign in
Appearance settings
Platform
AI CODE CREATION
GitHub Copilot Write better code with AI
GitHub Copilot app Direct agents from issue to merge
MCP Registry Integrate external tools
DEVELOPER WORKFLOWS
Actions Automate any workflow
Codespaces Instant dev environments
Issues Plan and track work
Code Review Manage code changes
Code Quality Enforce quality at merge
APPLICATION SECURITY
GitHub Advanced Security Find and fix vulnerabilities
Code security Secure your code as you build
Secret protection Stop leaks before they start
EXPLORE
Why GitHub
Documentation
Blog
Changelog
Marketplace View all features
Solutions
BY COMPANY SIZE
Enterprises
Small and medium teams
Startups
Nonprofits
BY USE CASE
App Modernization
DevSecOps
DevOps
CI/CD
View all use cases
BY INDUSTRY
Healthcare
Financial services
Manufacturing
Government
View all industries View all solutions
Resources
EXPLORE BY TOPIC
AI
Software Development
DevOps
Security
View all topics
EXPLORE BY TYPE
Customer stories
Events & webinars
Ebooks & reports
Business insights
GitHub Skills
SUPPORT & SERVICES
Documentation
Customer support
Community forum
Trust center
Partners View all resources
Open Source
COMMUNITY
GitHub Sponsors Fund open source developers
PROGRAMS
Security Lab
Maintainer Community
Accelerator
GitHub Stars
Archive Program
REPOSITORIES
Topics
Trending
Collections
Enterprise
ENTERPRISE SOLUTIONS
Enterprise platform AI-powered developer platform
AVAILABLE ADD-ONS
GitHub Advanced Security Enterprise-grade security features
Copilot for Business Enterprise-grade AI features
Premium Support Enterprise-grade 24/7 support
Pricing
Search or jump to...
Search code, repositories, users, issues, pull requests...
Search
Clear
Search syntax tips
Provide feedback
We read every piece of feedback, and take your input very seriously. [-]
Include my email address so I can be contacted
Cancel Submit feedback
Saved searches
Use saved searches to filter your results more quickly
Name
Query
To see all available qualifiers, see our documentation.
Cancel Create saved search
Sign in
Sign up
Appearance settings
Resetting focus
You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert
mpatacchiola / dissecting-reinforcement-learning Public
Notifications You must be signed in to change notification settings
Fork 178
Star 623
Code
Issues 4
Pull requests 0
Actions
Projects
Security and quality 0
Insights
Additional navigation options
Code
Issues
Pull requests
Actions
Projects
Security and quality
Insights 
Files Expand file tree
master
Breadcrumbs
dissecting-reinforcement-learning
/ environments
/
gridworld.py
Copy path
Blame
More file actions
Blame
More file actions
Latest commit
mpatacchiola
Adding the 'environments' folder and the README description
9 years ago
850c757
· 9 years ago
History
History
Open commit details 
History
178 lines (152 loc) · 7.97 KB
master
Breadcrumbs
dissecting-reinforcement-learning
/ environments
/
gridworld.py
Copy path
Top
File metadata and controls
Code
Blame
178 lines (152 loc) · 7.97 KB
Raw
Copy raw file
Download raw file
Open symbols panel
Edit and raw actions
#!/usr/bin/env python #MIT License #Copyright (c) 2017 Massimiliano Patacchiola # #Permission is hereby granted, free of charge, to any person obtaining a copy #of this software and associated documentation files (the "Software"), to deal #in the Software without restriction, including without limitation the rights #to use, copy, modify, merge, publish, distribute, sublicense, and/or sell #copies of the Software, and to permit persons to whom the Software is #furnished to do so, subject to the following conditions: # #The above copyright notice and this permission notice shall be included in all #copies or substantial portions of the Software. # #THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR #IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, #FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE #AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER #LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, #OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE #SOFTWARE. #Class for creating a gridworld of arbitrary size and with arbitrary obstacles. #Each state of the gridworld should have a reward. The transition matrix is defined #as the probability of executing an action given a command to the robot. import numpy as np class GridWorld: def init
(self, tot_row, tot_col): self.
action_space_size = 4 self.
world_row = tot_row self.
world_col = tot_col #The world is a matrix of size row x col x 2 #The first layer contains the obstacles #The second layer contains the rewards #self.
world_matrix = np.
zeros((tot_row, tot_col, 2)) self.
transition_matrix = np.
ones((self.
action_space_size, self.
action_space_size))/ self.
action_space_size #self.
transition_array = np.
ones(self.
action_space_size) / self.
action_space_size self.
reward_matrix = np.
zeros((tot_row, tot_col)) self.
state_matrix = np.
zeros((tot_row, tot_col)) self.
position = [np.
random.
randint(tot_row), np.
random.
randint(tot_col)] #def setTransitionArray(self, transition_array): #if(transition_array.
shape !
= self.
transition_array): #raise ValueError('The shape of the two matrices must be the same.
') #self.
transition_array = transition_array def setTransitionMatrix(self, transition_matrix): '''Set the reward matrix. 
The transition matrix here is intended as a matrix which has a line for each action and the element of the row are the probabilities to executes each action when a command is given. 
For example: [[0.55, 0.25, 0.10, 0.10] [0.25, 0.25, 0.25, 0.25] [0.30, 0.20, 0.40, 0.10] [0.10, 0.20, 0.10, 0.60]] This matrix defines the transition rules for all the 4 possible actions. 
The first row corresponds to the probabilities of executing each one of the 4 actions when the policy orders to the robot to go UP. 
In this case the transition model says that with a probability of 0.55 the robot will go UP, with a probaiblity of 0.25 RIGHT, 0.10 DOWN and 0.10 LEFT. 
''' if(transition_matrix.
shape !
= self.
transition_matrix.
shape): raise ValueError('The shape of the two matrices must be the same.
') self.
transition_matrix = transition_matrix def setRewardMatrix(self, reward_matrix): '''Set the reward matrix. 
''' if(reward_matrix.
shape !
= self.
reward_matrix.
shape): raise ValueError('The shape of the matrix does not match with the shape of the world.
') self.
reward_matrix = reward_matrix def setStateMatrix(self, state_matrix): '''Set the obstacles in the world. 
The input to the function is a matrix with the same size of the world -1 for states which are not walkable. 
+1 for terminal states 0 for all the walkable states (non terminal) The following matrix represents the 4x3 world used in the series "dissecting reinforcement learning" [[0, 0, 0, +1] [0, -1, 0, +1] [0, 0, 0, 0]] ''' if(state_matrix.
shape !
= self.
state_matrix.
shape): raise ValueError('The shape of the matrix does not match with the shape of the world.
') self.
state_matrix = state_matrix def setPosition(self, index_row=None, index_col=None): ''' Set the position of the robot in a specific state. 
''' if(index_row is None or index_col is None): self.
position = [np.
random.
randint(tot_row), np.
random.
randint(tot_col)] else: self.
position = [index_row, index_col] def render(self): ''' Print the current world in the terminal. 
O represents the robot position - respresent empty states. 
# represents obstacles * represents terminal states ''' graph = "" for row in range(self.
world_row): row_string = "" for col in range(self.
world_col): if(self.
position == [row, col]): row_string += u" \u25CB " # u" \u25CC " else: if(self.
state_matrix[row, col] == 0): row_string += ' - ' elif(self.
state_matrix[row, col] == -1): row_string += ' # ' elif(self.
state_matrix[row, col] == +1): row_string += ' * ' row_string += '\n' graph += row_string print graph def reset(self, exploring_starts=False): ''' Set the position of the robot in the bottom left corner. 
It returns the first observation ''' if exploring_starts: while(True): row = np.
random.
randint(0, self.
world_row) col = np.
random.
randint(0, self.
world_col) if(self.
state_matrix[row, col] == 0): break self.
position = [row, col] else: self.
position = [self.
world_row-1, 0] #reward = self.
reward_matrix[self.
position[0], self.
position[1]] return self.
position def step(self, action): ''' One step in the world. 
[observation, reward, done = env.
step(action)] The robot moves one step in the world based on the action given. 
The action can be 0=UP, 1=RIGHT, 2=DOWN, 3=LEFT @return observation the position of the robot after the step @return reward the reward associated with the next state @return done True if the state is terminal ''' if(action >= self.
action_space_size): raise ValueError('The action is not included in the action space.
') #Based on the current action and the probability derived #from the trasition model it chooses a new actio to perform action = np.
random.
choice(4, 1, p=self.
transition_matrix[int(action),:]) #action = self.
transition_model(action) #Generating a new position based on the current position and action if(action == 0): new_position = [self.
position[0]-1, self.
position[1]] #UP elif(action == 1): new_position = [self.
position[0], self.
position[1]+1] #RIGHT elif(action == 2): new_position = [self.
position[0]+1, self.
position[1]] #DOWN elif(action == 3): new_position = [self.
position[0], self.
position[1]-1] #LEFT else: raise ValueError('The action is not included in the action space.
') #Check if the new position is a valid position #print(self.
state_matrix) if (new_position[0]>=0 and new_position[0]<self.
world_row): if(new_position[1]>=0 and new_position[1]<self.
world_col): if(self.
state_matrix[new_position[0], new_position[1]] !
= -1): self.
position = new_position reward = self.
reward_matrix[self.
position[0], self.
position[1]] #Done is True if the state is a terminal state done = bool(self.
state_matrix[self.
position[0], self.
position[1]]) return self.
position, reward, done
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
Footer
© 2026 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Community
Docs
Contact
Manage cookies
Do not share my personal information
You can't perform that action at this time.
While the code is focused, press Alt+F1 for a menu of operations.