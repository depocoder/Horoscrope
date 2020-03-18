import random

times = ["Утром", "Днём", "Вечером", "Ночью", "После обеда", "Перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого.", "встреч со старыми знакомыми.",
            "неожиданного праздника.", "приятных перемен."]

def create_prophecies():
    generated_prophecies = []
    for i in range(5):
        generated_prophecies.append(str(i+1) +'. '+ random.choice(times)
        + " "+ random.choice(advices)
        + " " + random.choice(promises))
    return (generated_prophecies)