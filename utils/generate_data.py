import random
import string
import uuid
from datetime import datetime, timedelta
from playwright.sync_api import TimeoutError

def random_full_name_email():
    length = 12
    if length != 12:
        raise ValueError("Length must be exactly 12 to have a 9-character first name and a 2-character last name.")
    first_name_length = 9
    last_name_length = 2
    first_name = ''.join(random.choices(string.ascii_letters, k=first_name_length)).capitalize()
    last_name = ''.join(random.choices(string.ascii_letters, k=last_name_length)).capitalize()
    full_name = first_name + ' ' + last_name
    email = f"{first_name.lower()}.{last_name.lower()}@gmail.com"
    return full_name, email

def randomn_mobile_number():
    mobile_start_digit = random.choice('6789')
    mobile_number = mobile_start_digit + ''.join(random.choices(string.digits, k=9))
    return mobile_number

def randomn_dob():
    # Generate a random date of birth ensuring age is below 50 years and year is after 1975
    today = datetime.today()
    start_date = datetime.strptime('1976-01-01', '%Y-%m-%d')
    end_date = today - timedelta(days=365 * 18)  # Assuming a minimum age of 18
    random_days = random.randint(0, (end_date - start_date).days)
    date_of_birth = (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')
    return date_of_birth

def randomn_current_date():
    # Get the current date
    today = datetime.today()
    current_date = today.strftime('%Y-%m-%d')
    return current_date

def randomn_assessment_name_description():
    # Generate a random sports assessment name and related description 
    sports = ['Hockey', 'Football', 'Basketball', 'Swimming', 'Tennis', 'Cricket'] 
    descriptors = ['Performance', 'Skill', 'Fitness', 'Endurance', 'Strength', 'Agility'] 
    sport = random.choice(sports) 
    descriptor = random.choice(descriptors) 
    unique_id = uuid.uuid4().hex[:8] # Generate a short unique identifier
    
    assessment_name = f"{descriptor} {sport} Assessment {unique_id}" 
    assessment_description = f"This assessment focuses on evaluating the {descriptor.lower()} aspects of {sport.lower()}."
    return assessment_name, assessment_description

def randomn_address():
     # Generate a random Indian address with matched city, state, and postal code
    addresses = [
        {"city": "Mumbai", "state": "Maharashtra", "postal_code_range": range(400001, 400100)},
        {"city": "Delhi", "state": "Delhi", "postal_code_range": range(110001, 110100)},
        {"city": "Bangalore", "state": "Karnataka", "postal_code_range": range(560001, 560100)},
        {"city": "Chennai", "state": "Tamil Nadu", "postal_code_range": range(600001, 600100)},
        {"city": "Kolkata", "state": "West Bengal", "postal_code_range": range(700001, 700100)},
        {"city": "Hyderabad", "state": "Telangana", "postal_code_range": range(500001, 500100)},
        {"city": "Pune", "state": "Maharashtra", "postal_code_range": range(411001, 411100)}
    ]
    address = random.choice(addresses)
    city = address["city"]
    state = address["state"]
    postal_code = str(random.choice(address["postal_code_range"]))
    full_address = f"{random.choice(['MG Road', 'Brigade Road', 'Church Street'])}, {city}, {state}, {postal_code}"
    return full_address

def randomn_religion():
    # Generate random Indian religion 
    religions = ['Hindu', 'Muslim', 'Christian', 'Sikh', 'Buddhist', 'Jain'] 
    religion = random.choice(religions)
    return religion

def randomn_gender(page, gender_dropdown_locator): 
    # Select random gender value from the dropdown list 
    gender_dropdown = page.locator(gender_dropdown_locator)   # Locate the gender dropdown 
    options = gender_dropdown.locator('option').all_text_contents()     # Get all options within the dropdown 
    print("Available gender options:", options)     # Print all options (optional for debugging purposes)  
    random_gender_option = random.choice(options)      # Select a random option
    gender_dropdown.select_option(label=random_gender_option) 
    print(f"Selected gender: {random_gender_option}") 
    return random_gender_option

def randomn_caste(page, caste_dropdown_locator): 
    # Select random caste value from the dropdown list 
    caste_dropdown = page.locator(caste_dropdown_locator)   # Locate the caste dropdown 
    options = caste_dropdown.locator('option').all_text_contents()     # Get all options within the dropdown 
    print("Available caste options:", options)     # Print all options (optional for debugging purposes)  
    random_caste_option = random.choice(options)      # Select a random option
    caste_dropdown.select_option(label=random_caste_option) 
    print(f"Selected caste: {random_caste_option}") 
    return random_caste_option

def randomn_relation(): 
    relations = [ "Father", "Mother", "Brother", "Sister", "Uncle", "Aunt", "Cousin", "Grandfather", "Grandmother", "Son", "Daughter" ] 
    return random.choice(relations)

def randomn_sciencestaff_supportstaff(page, supportstaff_dropdown_locator): 
    # Select random supportstaff value from the dropdown list 
    supportstaff_dropdown = page.locator(supportstaff_dropdown_locator)   # Locate the supportstaff dropdown 
    options = supportstaff_dropdown.locator('option').all_text_contents()     # Get all options within the dropdown 
    print("Available supportstaff options:", options)     # Print all options (optional for debugging purposes)  
    random_supportstaff_option = random.choice(options)      # Select a random option
    supportstaff_dropdown.select_option(label=random_supportstaff_option) 
    print(f"Selected supportstaff: {random_supportstaff_option}") 
    return random_supportstaff_option

def randomn_player_class(page, player_class_dropdown_locator): 
    # Select random player value from the dropdown list 
    Player_class_dropdown = page.locator(player_class_dropdown_locator)   # Locate the player dropdown 
    options = Player_class_dropdown.locator('option').all_text_contents()     # Get all options within the dropdown 
    print("Available class options:", options)     # Print all options (optional for debugging purposes)  
    random_player_class_option = random.choice(options)      # Select a random option
    Player_class_dropdown.select_option(label=random_player_class_option) 
    print(f"Selected player class: {random_player_class_option}") 
    return random_player_class_option

def randomn_weight(): 
    weight = random.uniform(50, 60) # Generate random weight between 50 and 60 kg 
    return f"{round(weight, 2)}" # Convert to string format

def randomn_height(): 
    # Generate a random height in inches within the range 
    total_height_in_inches = random.uniform(60, 72) # 5 feet = 60 inches, 6 feet = 72 inches 
    height_in_feet = total_height_in_inches / 12 
    return f"{round(height_in_feet, 1)}" # Convert to string format

def randomn_allergies(): 
    allergies = ["None", "Peanuts", "Seafood", "Pollen", "Dust", "Latex", "Animal Dander"] 
    return random.choice(allergies) 

def randomn_current_medications(): 
    medications = ["None", "Ibuprofen", "Aspirin", "Metformin", "Lisinopril", "Omeprazole"] 
    return random.choice(medications) 

def randomn_previous_injuries(): 
    injuries = ["None", "Fracture", "Sprain", "Concussion", "Dislocation", "Muscle Tear"] 
    return random.choice(injuries)

def randomn_chronic_conditions(): 
    conditions = ["None", "Hypertension", "Diabetes", "Asthma", "Heart Disease"] 
    return random.choice(conditions) 

def randomn_surgeries(): 
    surgeries = ["None", "Appendectomy", "Gallbladder Removal", "Hernia Repair", "Heart Bypass"] 
    return random.choice(surgeries) 

def randomn_family_medical_history(): 
    history = ["None", "Diabetes", "Heart Disease", "Cancer", "Hypertension"] 
    return random.choice(history) 

def randomn_sleep_patterns(): 
    patterns = ["Regular", "Irregular", "Insomnia", "Hypersomnia"] 
    return random.choice(patterns) 

def randomn_diet(): 
    diets = ["Balanced", "Vegetarian", "Vegan", "Keto", "Mediterranean"] 
    return random.choice(diets) 

def randomn_hydration(): 
    hydration_levels = ["Adequate", "Inadequate", "Excessive"] 
    return random.choice(hydration_levels) 

def randomn_stress_levels(): 
    stress_levels = ["Low", "Moderate", "High"] 
    return random.choice(stress_levels)

def randomn_primary_sport(): 
    sports = ["Football", "Basketball", "Cricket", "Tennis", "Swimming"] 
    return random.choice(sports) 

def randomn_position_role(): 
    roles = ["Forward", "Defender", "Midfielder", "Goalkeeper", "Coach"] 
    return random.choice(roles) 

def randomn_secondary_sport(): 
    secondary_sports = ["Running", "Cycling", "Baseball", "Volleyball", "Badminton"] 
    return random.choice(secondary_sports) 

def randomn_event(): 
    events = ["100m Dash", "Marathon", "High Jump", "Long Jump", "Shot Put"] 
    return random.choice(events) 

def randomn_sports_category(): 
    categories = ["Junior", "Senior", "Amateur", "Professional", "Veteran"] 
    return random.choice(categories)

def randomn_coach(page, coach_dropdown_locator): 
    # Select random coach value from the dropdown list 
    coach_dropdown = page.locator(coach_dropdown_locator)   # Locate the coach dropdown 
    options = coach_dropdown.locator('option').all_text_contents()     # Get all options within the dropdown 
    print("Available coach options:", options)     # Print all options (optional for debugging purposes)  
    random_coach_option = random.choice(options)      # Select a random option
    coach_dropdown.select_option(value=random_coach_option) 
    print(f"Selected coach: {random_coach_option}") 
    return random_coach_option

def randomn_frequency_per_week(): 
    return str(random.randint(1, 7)) # Random frequency between 1 and 7 times per week 

def randomn_duration_per_session(): 
    return f"{random.randint(30, 120)}" # Random duration between 30 and 120 minutes 

def randomn_participation(): 
    participation_types = ["Practice", "Competition", "Training Camp", "Friendly Match"] 
    return random.choice(participation_types) 

def randomn_medal_won(page, medal_dropdown_locator): 
    # Select random medal value from the dropdown list 
    medal_dropdown = page.locator(medal_dropdown_locator)   # Locate the medal dropdown 
    options = medal_dropdown.locator('option').all_text_contents()     # Get all options within the dropdown 
    print("Available medal options:", options)     # Print all options (optional for debugging purposes)  
    random_medal_option = random.choice(options)      # Select a random option
    medal_dropdown.select_option(value=random_medal_option) 
    print(f"Selected medal: {random_medal_option}") 
    return random_medal_option

def randomn_short_term_goals(): 
    sgoals = [ "Improve speed", "Enhance stamina", "Master new techniques", "Increase flexibility", "Reduce injury risk" ] 
    return random.choice(sgoals) 

def randomn_long_term_goals(): 
    lgoals = [ "Win a national championship", "Qualify for the Olympics", "Become a professional athlete", "Set a new personal record", "Join a prestigious sports club" ] 
    return random.choice(lgoals)

def randomn_sports_organization_names(num_names=10): 
    adjectives = ["Elite", "Dynamic", "Power", "Global", "Ultimate", "Prime", "Victory", "Champion", "Epic", "Supreme"] 
    sports_types = ["Soccer", "Basketball", "Tennis", "Cricket", "Rugby", "Athletics", "Swimming", "Volleyball", "Hockey", "Baseball"] 
    organization_types = ["Club", "Association", "League", "Academy", "Federation", "Union", "Network", "Group", "Team", "Council"] 
    names = [] 
    for _ in range(num_names): 
        adjective = random.choice(adjectives) 
        sport = random.choice(sports_types) 
        org_type = random.choice(organization_types) 
        name = f"{adjective} {sport} {org_type}" 
        names.append(name) 
        return names

def randomn_short_indian_sports_team_names(num_names=10): 
    cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Ahmedabad", "Pune", "Jaipur", "Lucknow"] 
    team_types = ["Warriors", "Eagles", "Panthers", "Tigers", "Hawks", "Wolves", "Knights", "Dragons", "Sharks", "Lions"] 
    names = [] 
    for _ in range(num_names): 
        city = random.choice(cities) 
        team_type = random.choice(team_types) 
        name = f"{city} {team_type}" 
        names.append(name) 
        return names

def randomn_organization_name(page, dropdown_locator): 
    try: 
        # Click to open the dropdown 
        organization_dropdown = page.locator(dropdown_locator) 
        organization_dropdown.wait_for(state='visible') 
        organization_dropdown.click() 
        # Wait for the dropdown options to appear 
        page.wait_for_selector('.ng-dropdown-panel .ng-option:not(:has-text("Select Organization"))', state='visible')
        # Retrieve all options within the dropdown, excluding the "Select Organization" option
        options = page.locator('.ng-dropdown-panel .ng-option:not(:has-text("Select Organization"))')
        option_count = options.count() 
        if option_count == 0: 
            raise ValueError('No options found in the dropdown.') 
        # Get all options text 
        options_text = options.all_text_contents() 
        print("Available Organization options:", options_text)  # Print all options (optional for debugging purposes) 
        # Select a random option 
        random_option_text = random.choice(options_text) 
        options.locator(f'text={random_option_text}').click() 
        print(f"Selected Organization: {random_option_text}") 
        return random_option_text 
    except Exception as e: 
        print(f"An error occurred: {e}")

def randomn_select_sports_name(page, dropdown_locator): 
    try: 
        # Click to open the dropdown 
        sports_dropdown = page.locator(dropdown_locator) 
        sports_dropdown.wait_for(state='visible') 
        sports_dropdown.click() 
        # Wait for the dropdown options to appear 
        page.wait_for_selector('.ng-dropdown-panel .ng-option', state='visible') 
        # Retrieve all options within the dropdown, excluding the "Select Organization" option
        options = page.locator('.ng-dropdown-panel .ng-option:not(:has-text("Select Sport"))')
        option_count = options.count() 
        if option_count == 0: 
            raise ValueError('No options found in the dropdown.') 
        # Get all options text 
        options_text = options.all_text_contents() 
        print("Available Sports options:", options_text)  # Print all options (optional for debugging purposes) 
        # Select a random option 
        random_option_text = random.choice(options_text) 
        options.locator(f'text={random_option_text}').click() 
        print(f"Selected Organization: {random_option_text}") 
        return random_option_text 
    except TimeoutError as e: 
        print(f"TimeoutError occurred: {e}")
        
        
def select_random_coach_sport(page, dropdown_locator): 
    try: 
        # Click to open the dropdown 
        sport_dropdown = page.locator(dropdown_locator) 
        sport_dropdown.wait_for(state='attached')
        sport_dropdown.click() 
        # Wait for the dropdown options to appear 
        page.wait_for_selector('select[name="usrSport"] option', state='visible') 
        # Retrieve all options within the dropdown, excluding the "Select Sport" option 
        options = page.locator('select[name="usrSport"] option:not([value=""])') 
        option_count = options.count()
        if option_count == 0: 
            raise ValueError('No options found in the dropdown.') 
        # Get all options text 
        options_text = options.all_text_contents() 
        print("Available Sport options:", options_text)  # Print all options (optional for debugging purposes) 
        # Select a random option 
        random_option = random.choice(options.element_handles()) 
        random_option_value = random_option.get_attribute('value') 
        page.select_option('select[name="usrSport"]', value=random_option_value) 
        selected_option_text = random_option.text_content() 
        print(f"Selected Sport: {selected_option_text}")
        return selected_option_text
    except TimeoutError as e: 
        print(f"TimeoutError occurred: {e}") 
        raise