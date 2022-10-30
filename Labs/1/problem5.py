import pandas as pd 
import math
def main():
    print("Solution For Problem 5, Homework 1, Data Science Lab")

    patient_data = pd.read_csv("PatientData.csv", header = None)
    
    print("(a)\nThere are " + str(len(patient_data)) + " Patients in the DataFrame")
    print("\nThere are " + str(len(patient_data.columns) - 1) + " Features in the DataFrame")

    print("\n(b)\nThe first feature represents age in years")
    print("The second feature represents sex (0 for men, 1 for women)")
    print("The third feature represents height in centimeters")
    print("The fourth feature represents weight in kg")

    print("\n(c)\nYes there are missing values")

    # Replace each question mark with the average for each feature
    col = 1
    for label, feature in patient_data.iteritems():
        # Compute the avg
        avg = 0
        for value in feature.iteritems():
            if value[1] != "?":
                avg += float(value[1])    
        avg /= len(feature)
        patient_data[label] = feature.replace(to_replace = "?", value = avg)
    
    # Compute the correlation coefficient
    print("\n(d)\nWe can determine which features influence the patient condition by computing \nthe correlation Coeff between the feature and the results and finding the ones closest to -1 and 1")

    corr = patient_data.corr()
    coeff = []
    for pair in corr[len(patient_data.columns) - 1].iteritems():
        if not math.isnan(pair[1]):
            coeff.append((pair[0], abs(pair[1])))
        
    coeff.sort(key = lambda x: x[1])
    coeff.reverse()
    # Record the most useful
    print("\nThe following indices repreesent the 3 features that are most correlated with patient results:")
    for i in range(1, 4):
        print(coeff[i][0], end = " ")
    print("\nNote: we ignore the first one, because the most correlated value computed witht the result was itself")
if __name__ == "__main__":
    main()