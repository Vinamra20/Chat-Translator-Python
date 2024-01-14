from googletrans import Translator


class ChatTranslator:
    def __init__(self):
        self.translator = Translator()

    def translate_message(self, message, target_language):
        translation = self.translator.translate(message, dest=target_language)
        return translation.text

    def chat_between_users(self, user_message, user_language, other_language):
        # Translate user's message to the other user's language
        other_user_message = self.translate_message(
            user_message, other_language)

        # Return translated message for the other user
        return other_user_message


if __name__ == "__main__":
    chat_translator = ChatTranslator()

    # Get user1's input
    user1_language = input(
        "User 1, select your language (en, hi, ml, ta, te, ru, zh, fr, de, pl, ar): ").lower()

    # Get user2's input
    user2_language = input(
        "User 2, select your language (en, hi, ml, ta, te, ru, zh, fr, de, pl, ar): ").lower()

    while True:
        # User 1 sends a message
        user1_message = input(
            "\nUser 1, enter your message (type 'exit' to end the chat): ")
        if user1_message.lower() == 'exit':
            break

        # Translate and print the conversation
        user2_message = chat_translator.chat_between_users(
            user1_message, user1_language, user2_language)
        print(f"\nUser 1 ({user1_language}): {user1_message}")
        print(f"User 2 ({user2_language}): {user2_message}")

        # User 2 sends a message
        user2_message = input(
            "\nUser 2, enter your message (type 'exit' to end the chat): ")
        if user2_message.lower() == 'exit':
            break

        # Translate and print the conversation
        user1_message = chat_translator.chat_between_users(
            user2_message, user2_language, user1_language)
        print(f"\nUser 2 ({user2_language}): {user2_message}")
        print(f"User 1 ({user1_language}): {user1_message}")


# download these librariues before running the code - pip install translate, pip install googletrans==4.0.0-rc1
