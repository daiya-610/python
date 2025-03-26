from roboter.models.ranking import RankingModel
from roboter.models.robot import Robot


def talk_about_restaurant():
    robot = Robot()
    robot.hello()

    ranking = RankingModel()
    while True:
        restaurant = input("What is your favorite restaurant? ")
        ranking.increment(restaurant)
        print(f"Thanks! {restaurant} has been added to the rankning.")

        another = input("Do you want to add another restaurant? (yes/no)")
        if another.lower() != "yes":
            break

    most_popular = ranking.get_most_popular()
    print(f"The most popular restaurant is {most_popular}!")
