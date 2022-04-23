from BonanzaBot import *

def run(config: list):
    
    craft = Aircraft(config[0])
    craft.start()
    
    geo = Geocoode([config[1]])
    
    while True:
        ### Big loop to check if aircraft alive or not.
        ## If alive, takeoff or landing?
        exit()
    
def getConfig(path) -> list:
    with open(path) as file:
        raw_config = file.readlines()
    config = [i.strip() for i in raw_config]
    return config

if __name__ == "__main__":
    config = getConfig("config/config.txt")
    run(config)