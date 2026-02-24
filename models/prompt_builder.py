def build_prompt(data):
    return f"""
    Generate a professional ATS-optimized resume and cover letter.

    Name: {data['name']}
    Email: {data['email']}
    Education: {data['education']}
    Skills: {data['skills']}
    Projects: {data['projects']}
    Target Role: {data['target_role']}

    Make it achievement-oriented and impactful.
    """