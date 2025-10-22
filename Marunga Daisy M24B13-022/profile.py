 class profile:
    def __init__ (
        self, name, favorite_language, hobby, tech_stack, github_username, fun_fact):
        self.name = name
        self.favorite_language = favorite_language
        self.hobby = hobby 
        self.tech_stack = tech_stack
        self.github_username = github_username
        self.fun_fact = fun_fact
        
    def introduce(self):
        print(
            f"hi, i am {self.name}. i love {self.favorite_language} and my hobby is {self.hobby}."
        )
        print(f"fun fact about me: {self.fun_fact}")
        
    def show_stack(self):
        print(f"{self.name}'s tech stack:")
        for i, tool in enumerate(self.tech_stack, start=1):
            print(f"{i}. {tool}")
            
    def github_link(self):
        return f"https://github.com/{self.github_username}"
    
    

#creating my profile
my_profile = profile(
    name="Marunga Daisy",
    favorite_language="python",
    hobby="watching movies",
    tech_stack=["canva", "javascript", "CSS", "React", "HTML", "Next.js"],
    github_username="DaisyMO2", 
    fun_fact="i love travelling but i have travelling sickness!",
)

#calling the methods
my_profile.introduce()
print()
my_profile.show_stack()
print()
print("github profile:", my_profile.github_link())
