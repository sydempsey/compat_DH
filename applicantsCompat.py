import json
import math


#####################################
#########   functions   #############
#####################################

#returns average value in array
def avg(arr):
    return sum(arr) / float(len(arr))

#gets attributes for specified team or applicants
def get_attributes(empl,att):
    team_access = read_content[empl]
    save_data = []
    for attributes_data in team_access:
        attribute_access = attributes_data['attributes'][att]
        save_data.append(attribute_access)
        #print(attribute_access)
    return save_data

#Stores Applicant name and attribute scores into an array
def get_app_info(num):
    info = []
    applicant_access = read_content['applicants'][num]
    data = applicant_access['attributes']

    #Add attributes of applicant to []
    info.append(applicant_access['name'])
    info.append(data['intelligence'])
    info.append(data['strength'])
    info.append(data['endurance'])
    info.append(data['spicyFoodTolerance'])

    #print(info)
    return info


#Calculate Compatibility for each applicant
def calc_compat(applicant_arr, t_intel, t_str, t_end, t_spicy):
    intelligence = applicant_arr[1]
    strength = applicant_arr[2]
    endurance = applicant_arr[3]
    spicy = applicant_arr[4]
    final = []
    final.append(applicant_arr[0])

    #Calc % and rank by importance
    if intelligence > t_intel:
        intelligence = (t_intel/intelligence)*0.5
    else:
        intelligence = (intelligence/t_intel)*0.5

    if strength > t_str:
        strength = (t_str/strength)*0.1
    else:
        strength = (strength/t_str)*0.1

    if endurance > t_end:
        endurance = (t_end/endurance)*0.35
    else:
        endurance = (endurance/t_end)*0.35

    if spicy > t_spicy:
        spicy = (t_spicy/spicy)*0.05
    else:
        spicy = (spicy/t_spicy)*0.05

    #Sum up the applicants total score and add to array
    score = intelligence + strength + endurance + spicy 
    final.append(score)
    return final



#####################################
#########     Main      #############
#####################################

#Open data file
data = json.load(open('data.json'))


#store data in a python object - type = dict
with open('data.json') as access_json:
    read_content = json.load(access_json)

#function call to store team's attributes into arrays
teams_intelligence = get_attributes('team','intelligence')
teams_strength = get_attributes('team','strength')
teams_endurance = get_attributes('team','endurance')
teams_spicy = get_attributes('team','spicyFoodTolerance')

#Find average team values for each attribute
intel_avg = avg(teams_intelligence)
strength_avg = avg(teams_strength)
endurance_avg = avg(teams_endurance)
spicy_avg = avg(teams_spicy)


#Get Applicants Info
app1 = get_app_info(0)
app2 = get_app_info(1)
app3 = get_app_info(2)

#Get score of each applicant
app1 = calc_compat(app1,intel_avg,strength_avg,endurance_avg,spicy_avg)
app2 = calc_compat(app2,intel_avg,strength_avg,endurance_avg,spicy_avg)
app3 = calc_compat(app3,intel_avg,strength_avg,endurance_avg,spicy_avg)


data = {'scoredApplicants': [
        {
            'name': app1[0],
            'score': app1[1]
        },{
            'name': app2[0],
            'score': app2[1]
        },{
            'name': app3[0],
            'score': app3[1]
        }
    ]
 }


#write applicants and scores to json file
with open('scoredApplicants.json', "w") as file:
    json.dump(data,file,indent=4, sort_keys=True)

    
