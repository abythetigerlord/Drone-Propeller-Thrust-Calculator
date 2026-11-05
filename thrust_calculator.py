"""Estimate drone thrust and thrust-to-weight ratio."""


GRAVITY = 9.80665


def calculate_thrust(motor_count, thrust_per_motor_g, aircraft_mass_g):
    """Return total thrust, thrust-to-weight ratio, and lift capability."""
    if motor_count <= 0 or thrust_per_motor_g <= 0 or aircraft_mass_g <= 0:
        raise ValueError("All values must be positive.")
    total_thrust_g = motor_count * thrust_per_motor_g
    ratio = total_thrust_g / aircraft_mass_g
    total_thrust_n = total_thrust_g / 1000 * GRAVITY
    return {
        "total_thrust_g": total_thrust_g,
        "total_thrust_n": total_thrust_n,
        "thrust_to_weight_ratio": ratio,
        "can_hover": ratio >= 1.0,
        "recommended_for_control": ratio >= 2.0,
    }


def main():
    print("Drone Propeller Thrust Calculator")
    motors = int(input("Number of motors: "))
    thrust = float(input("Thrust per motor (g): "))
    mass = float(input("Total drone mass (g): "))
    result = calculate_thrust(motors, thrust, mass)
    print(f"\nTotal thrust: {result['total_thrust_g']:.0f} g ({result['total_thrust_n']:.2f} N)")
    print(f"Thrust-to-weight ratio: {result['thrust_to_weight_ratio']:.2f}:1")
    print("Can hover: " + ("Yes" if result["can_hover"] else "No"))
    print("Recommended control margin: " + ("Yes" if result["recommended_for_control"] else "No"))


if __name__ == "__main__":
    main()

