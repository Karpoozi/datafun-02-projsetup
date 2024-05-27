# Brooke Richards Project 1 Start
''' 
This module provides a reusable byline for the author's services.
'''

# Import Dependencies
import math
import statistics

# Define Variables 
company_name: str = "Karpoozi Konsultants"
description: str = "An Athens-based educational consultancy company specializing in guiding individuals through the complex process of pursuing higher education opportunities abroad."
company_email: str = "goabroad@karpoozi.ga"
services: list = ["Academic Advisement", "Test Preparation", "Language Learning", "Application Assistance", "Visa Counseling", "Financial Planning"]
count_active_countries: int = 22
client_act_scores: list = [17, 20, 25, 32, 22]
average_client_satisfaction: float = 4.4
has_international_presence: bool = True

# Define Formatted Strings
active_countries_string: str = f"Active Countries: {count_active_countries}"
international_presence_string: str = f"International Presence: {has_international_presence}"
client_satisfaction_string: str = f"Average Client Satisfaction Score: {average_client_satisfaction}"
services_string: str = f"Services Offered: {', '.join(services)}"

# Calculate Descriptive Statistics
num_clients = len(client_act_scores)
lowest_score = min(client_act_scores)
highest_score = max(client_act_scores)
mean_score = statistics.mean(client_act_scores)
rounded_mean_score = math.floor(mean_score)
mode_score = statistics.mode(client_act_scores)
median_score = statistics.median(client_act_scores)

stats_string: str = f"""
Descriptive Statistics for Our Clients Average ACT Scores:
Smallest: {lowest_score}
Largest: {highest_score}
Count: {num_clients}
Mean: {rounded_mean_score}
Mode: {mode_score}
Median: {median_score}
"""

# Define Byline String
byline: str = f"""
{company_name}
{active_countries_string}
{client_satisfaction_string}
{services_string}
{stats_string}
"""

# Define Main Function
def main():
    '''Display all output'''
    print(byline)
    
# Conditional Script Execution
if __name__ == '__main__':
    main()
