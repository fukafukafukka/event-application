from __future__ import annotations
import math

class TankBody:
    def __init__(self, name: str, position_x = 0, position_y = 0, be_shot_count = 0):
        self.position_x = position_x
        self.position_y = position_y
        self.name = name
        self.engine = None
        self.gun = None
        self.caterpillar = None
        self.fuel_tank = None
        self.WEIGHT = 10000
        self.crew_list = []
        self.be_shot_count = 0
        self.NECESSARY_FUEL_TO_ROTATE_90_DEGREES = 4
        self.CAPACITY_OF_CREW = 2
        self.NECESSARY_FUEL_TO_START_ENGINE = 10
        self.NECESSARY_FUEL_RATE_TO_MOVE_100_METERS = 0.04
        self.NECESSARY_FUEL_TO_MOVE_100_METERS = 4
        self.LIMIT_TO_BE_SHOT = 10

    def set_fuel_tank(self, fuel_tank: fuel_tank):
        self.fuel_tank = fuel_tank
        print(f"{self.fuel_tank.name}を車体にセットしました。")

    def set_engine(self, engine: engine):
        self.engine = engine
        print(f"{self.engine.name}を車体にセットしました。")

    def set_gun(self, gun: gun):
        self.gun = gun
        print(f"{self.gun.name}を車体にセットしました。")

    def set_on_caterpillar(self, caterpillar: caterpillar):
        self.caterpillar = caterpillar
        self.position_x = self.caterpillar.get_position_x()
        self.position_y = self.caterpillar.get_position_y()
        print(f"{self.caterpillar.name}を車体にセットしました。")

    def supply(self, fuel):
        if self.fuel_tank_has_set() == False:
            return False
        self.fuel_tank.supply(fuel)
        return True

    def start_engine(self):
        if self.engine_has_set() == False:
            return False
        if self.engine.working == True:
            print('エンジンは起動済みです。')
            return False
        if self.fuel_tank_has_set() == False:
            return False
        if self.fuel_tank.consume(self.NECESSARY_FUEL_TO_START_ENGINE) == True:
            self.engine.start()
            print('エンジンを起動しました。')
            return True
        else:
            print('燃料が足りずエンジンを起動できません。')
            return False

    def stop_engine(self):
        if self.engine_has_set() == True:
            self.engine.stop()
            print('エンジンを停止しました。')
            return True
        else:
            return False

    def caterpillar_turn_left(self):
        if self.caterpillar_has_set() == False:
            return False
        if  self.check_crew_fuel_tank_and_engine(self.NECESSARY_FUEL_TO_ROTATE_90_DEGREES) == True:
            self.caterpillar.turn_left()
            return True
        else:
            return False

    def caterpillar_turn_right(self):
        if self.caterpillar_has_set() == False:
            return False
        if  self.check_crew_fuel_tank_and_engine(self.NECESSARY_FUEL_TO_ROTATE_90_DEGREES) == True:
            self.caterpillar.turn_right()
            return True
        else:
            return False

    def caterpillar_turn_back(self):
        if self.caterpillar_has_set() == False:
            return False
        if self.check_crew_fuel_tank_and_engine(self.NECESSARY_FUEL_TO_ROTATE_90_DEGREES * 2) == True:
            self.caterpillar.turn_back()
            return True
        else:
            return False

    def get_direction(self) -> direction_name:
        if self.caterpillar_has_set() == True:
            return self.caterpillar.get_direction()
        else:
            return False

    def move(self, move_distance: move_distance):
        if self.caterpillar_has_set() == False:
            return False
        if move_distance % 100 != 0:
            print('移動距離は100の整数値の倍数でないと動きません。')
            return False
        if self.check_engine() == False:
            return False
        if self.check_crew() == False:
            return False
        if self.fuel_tank.fuel >= move_distance * self.NECESSARY_FUEL_RATE_TO_MOVE_100_METERS:
            self.fuel_tank.consume(move_distance * self.NECESSARY_FUEL_RATE_TO_MOVE_100_METERS)
            self.caterpillar.move(move_distance)
            return True
        elif self.fuel_tank.fuel >= self.NECESSARY_FUEL_TO_MOVE_100_METERS:
            move_distance_when_not_much_of_fuel = int(self.fuel_tank.fuel / self.NECESSARY_FUEL_TO_MOVE_100_METERS) * 100
            self.fuel_tank.consume(self.fuel_tank.fuel)
            self.caterpillar.move(move_distance_when_not_much_of_fuel)
            return True
        else:
            print('燃料が足りません。')
            return False

    def get_position_x(self) -> int:
        if self.caterpillar == None:
            return self.position_x
        else:
            return self.caterpillar.get_position_x()

    def get_position_y(self) -> int:
        if self.caterpillar == None:
            return self.position_y
        else:
            return self.caterpillar.get_position_y()

    def get_position_coordinate(self):
        if self.caterpillar == None:
            return self.position_x, self.position_y
        else:
            return self.caterpillar.get_position_coordinate()

    def gun_turn_right(self):
        if self.gun_has_set() == False:
            return False
        if self.check_crew_fuel_tank_and_engine(self.NECESSARY_FUEL_TO_ROTATE_90_DEGREES) == True:
            self.gun.turn_right()
            return True
        else:
            return False

    def gun_turn_left(self):
        if self.gun_has_set() == False:
            return False
        if self.check_crew_fuel_tank_and_engine(self.NECESSARY_FUEL_TO_ROTATE_90_DEGREES) == True:
            self.gun.turn_left()
            return True
        else:
            return False

    def gun_turn_back(self):
        if self.gun_has_set() == False:
            return False
        if self.check_crew_fuel_tank_and_engine(self.NECESSARY_FUEL_TO_ROTATE_90_DEGREES * 2) == True:
            self.gun.turn_back()
            return True
        else:
            return False

    def get_gun_direction(self) -> direction_name:
        if self.gun_has_set() == True:
            return self.gun.get_direction()
        else:
            return False

    def add_shells(self, shell: shell):
        if self.gun_has_set() == True:
            return self.gun.add_shells(shell)
        else:
            return False

    def get_shell_quantity(self) -> int:
        if self.gun_has_set() == True:
            return self.gun.check_shell_quantity()
        else:
            return False

    def fire(self):
        if self.fuel_tank == None or self.fuel_tank.fuel == 0:
            print('燃料を搭載・足してから発射してください。')
            return False
        if self.gun_has_set() == True and self.check_crew() == True and self.check_engine() == True:
            return self.gun.fire(self.get_position_x(), self.get_position_y(), self.fuel_tank)
        else:
            return False

    def be_shot(self, quantity_of_hit_bullet):
        self.be_shot_count += quantity_of_hit_bullet
        if self.be_shot_count >= self.LIMIT_TO_BE_SHOT:
            self.engine.stop()
            print('被弾によりエンジンが止まりました！')
            self.be_shot_count = 0

    def ride_on(self, human):
        if len(self.crew_list) >= self.CAPACITY_OF_CREW:
            print('定員オーバーのため搭乗させられません。')
            return False
        else:
            self.crew_list.append(human)
            print(f'{human.name}を搭乗させました。')
            return True

    def get_weight(self) -> int:
        gun_weight = 0
        crew_weights = 0
        fuel_tank_weight = 0
        if self.gun != None:
            gun_weight = self.gun.get_weight()
        if len(self.crew_list) > 0:
            for crew in self.crew_list:
                crew_weights += crew.get_weight()
        if self.fuel_tank != None:
            fuel_tank_weight = self.fuel_tank.get_weight()
        return self.WEIGHT + gun_weight + crew_weights + fuel_tank_weight

    def check_crew_fuel_tank_and_engine(self, necessary_fuel: int):
        if len(self.crew_list) < self.CAPACITY_OF_CREW:
            print('乗務員が足りません。')
            return False
        if self.fuel_tank == None or self.fuel_tank.consume(necessary_fuel) == False:
            print('燃料タンクを搭載、もしくは燃料を足してください。')
            return False
        elif self.check_engine() == True:
            return True

    def check_crew(self):
        if len(self.crew_list) == self.CAPACITY_OF_CREW:
            return True
        else:
            print('乗務員が足りません。')
            return False

    def fuel_tank_has_set(self):
        if self.fuel_tank == None:
            print('燃料タンクを搭載してください。')
            return False
        else:
            return True

    def check_engine(self):
        if self.engine == None or self.engine.working == False:
            print('エンジンを搭載・起動してください。')
            return False
        else:
            return True

    def engine_has_set(self):
        if self.engine == None:
            print('エンジンを搭載してください。')
            return False
        else:
            return True

    def caterpillar_has_set(self):
        if self.caterpillar == None:
            print('キャタピラに搭載してください。')
            return False
        else:
            return True

    def gun_has_set(self):
        if self.gun == None:
            print('Gunを搭載してください。')
            return False
        else:
            return True