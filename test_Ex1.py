import pytest
from ExDebug1 import environnement_optimal
def test_environnement_optimal():
   ##Arrange: préparer les valeurs des variables d'entrées et le resultat attendu
    temperature = 25
    poussiere = "faible"
    humidite = 40
    resultat_attendu = "Tout est sous contrôle!"

   ##Act: appeler la fonction
    resultat_obtenu = environnement_optimal(temperature, poussiere, humidite)

   ##assert: verifier si le resultat obtenu correspond au resultat attendu
    assert resultat_attendu == resultat_obtenu


def test_environnement_optimal_2():
 ##Arrange: préparer les valeurs des variables d'entrées et le resultat attendu
 temperature = 30
 poussiere = "faible"
 humidite = 40
 resultat_attendu = "Environnement non optimal"

 ##Act: appeler la fonction
 resultat_obtenu = environnement_optimal(temperature, poussiere, humidite)

 ##assert: verifier si le resultat obtenu correspond au resultat attendu
 assert resultat_attendu == resultat_obtenu