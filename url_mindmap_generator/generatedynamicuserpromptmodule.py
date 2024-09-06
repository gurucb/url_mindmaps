def generate_dynamic_user_prompt(base_url):
        # Extract key parts of the URL to form a dynamic user prompt
        # For example, we can extract keywords from the URL path and build a context-specific prompt
        path_parts = base_url.split('/')
        context = path_parts[-2].replace('-', ' ') if len(path_parts) > 1 else "reliability design principles"

        # Create the dynamic user prompt based on extracted context
        user_prompt = f"I'm interested in learning about {context}. Can you provide a summary of each section?"

        return user_prompt