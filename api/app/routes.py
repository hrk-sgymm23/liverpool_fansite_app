from config import Config
from controllers import players_controller, matches_controller

def register_routes(app):
    API_V1_PATH = Config.API_V1_PATH

    # player
    app.add_url_rule(
        f"{API_V1_PATH}/players",
        'get_players', 
        players_controller.get_players,
        methods=['GET']
    )

    # match
    app.add_url_rule(
        f"{API_V1_PATH}/matches",
        'get_matches',
        matches_controller.get_matches,
        methods=['GET']
    )
    app.add_url_rule(
        f"{API_V1_PATH}/recent_result",
        'get_recent_match_result',
        matches_controller.get_recent_match_result,
        methods=['GET']
    )