from facade.linkedin_routine_facade import LinkedinRoutineFacade
from config import config
from util.dependencies import check_dependencies
from manager.auth_manager import AuthManager
from manager.connect_with_people import ConnectWithPeopleManager
from manager.feed_like_manager import FeedLikeManager

def main():
    """Função principal para execução do bot"""
    print("=== LinkedIn Automation Bot with Chromium ===")
    
    check_dependencies()

    auth = AuthManager(config['credentials'])
    connections = ConnectWithPeopleManager(config['target_criteria'])
    feed_like = FeedLikeManager()

    LinkedinRoutineFacade(auth,connections,feed_like).execute()

if __name__ == "__main__":
    main()