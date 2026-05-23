import os
import json
from groq import Groq
from dotenv import load_dotenv
from src.agent import CodeReviewAgent
from src.tools import read_file

# for user input of code
def get_code_input():
    print("\nPaste your UiPath code below")
    print("When done → type 'end' on a new line and press Enter")
    print("-"*50)
    
    lines = []
    while True:
        line = input()
        if line.strip().lower() == "end":
            break
        lines.append(line)
    
    return "\n".join(lines)

def main():
    # Load env
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")

    # Check API key exists
    if not api_key:
        print("❌ API key not found. Check your .env file")
        return

    # Create Groq client and agent
    client = Groq(api_key=api_key)
    agent = CodeReviewAgent(groq_client=client)

    # Welcome message
    print("="*50)
    print("🤖 UIPATH CODE REVIEWER AGENT")
    print("="*50)

    # Main loop
    while True:
        print("\nOptions:")
        print("1 → Review Code")
        print("2 → Clear History")
        print("3 → Exit")

        choice = input("\nEnter choice (1/2/3): ").strip()

        if choice == "1":
            print("\n1 → Paste the direct code")
            print("2 → Paste the file path")
            sub_choice = input("\nEnter choice (1/2): ").strip()

            if sub_choice == "1":
                code = get_code_input()
                if not code.strip():
                    print("❌ No code entered")
                    continue

            elif sub_choice == "2":
                file_path = input("\nEnter file path: ").strip()
                success, code = read_file(file_path)
                if not success:
                    print(f"❌ {code}")
                    continue

            else:
                print("❌ Invalid choice")
                continue

            print("\n⏳ Reviewing your code...")
            review = agent.code_review(code)

            print("\n" + "="*50)
            print(f"⭐ Overall Score: {review['overall_score']}/10")
            print(f"📝 Summary: {review['summary']}")

            print("\n🔍 LAYER 1 - SYNTAX")
            print(json.dumps(review['layer1_syntax'], indent=4))

            print("\n📐 LAYER 2 - QUALITY")
            print(json.dumps(review['layer2_quality'], indent=4))

            print("\n🧠 LAYER 3 - LOGIC")
            print(json.dumps(review['layer3_logic'], indent=4))

            print("\n💡 LAYER 4 - SUGGESTIONS")
            print(json.dumps(review['layer4_suggestions'], indent=4))
            print("="*50)

        elif choice == "2":
            print(agent.history)
            agent.clear_history()

        elif choice == "3":
            print("\n👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()