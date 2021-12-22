# Do not modify these lines
__winc_id__ = "7b9401ad7f544be2a23321292dd61cb6"
__human_name__ = "arguments"

# Add your code after this line

# part 1: greet template


def greet(name, greeting_template="Hello, <name>!"):
    greeting = (
        greeting_template[0 : greeting_template.find("<")]
        + name
        + greeting_template[greeting_template.find(">") + 1 :]
    )
    return greeting


# part 2: force = mass * gravity


def force(mass, body="earth"):
    planet_mass = {
        "sun": 274.0,
        "jupiter": 24.9,
        "neptune": 11.2,
        "saturn": 10.4,
        "earth": 9.8,
        "uranus": 8.9,
        "venus": 8.9,
        "mars": 3.7,
        "mercury": 3.7,
        "moon": 1.6,
        "pluto": 0.6,
    }
    if planet_mass.get(body, "not_existing") == "not_existing":
        return "body does not exist"
    else:
        force_calculation = mass * planet_mass.get(body)
        return force_calculation


# part 3: gravity


def pull(m1, m2, d):
    G = 6.674 * 10 ** -11
    pull_calculation = G * ((m1 * m2) / d ** 2)
    return pull_calculation
