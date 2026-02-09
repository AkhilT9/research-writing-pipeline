from dotenv import load_dotenv
load_dotenv()

from crew import crew

if __name__ == "__main__":
    result = crew.kickoff()
    print("\nFINAL OUTPUT:\n")
    print(result)
