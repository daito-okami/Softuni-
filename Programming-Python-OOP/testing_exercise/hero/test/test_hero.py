from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.main_hero = Hero('Daito', 5, 100, 10)
        self.hiro = Hero('Hiro', 10, 80, 20)

    def test_check_attribute_are_set(self):
        self.assertEqual('Daito', self.main_hero.username)
        self.assertEqual(5, self.main_hero.level)
        self.assertEqual(100, self.main_hero.health)
        self.assertEqual(10, self.main_hero.damage)

    def test_battle_raises_fighting_yourself(self):
        hero_self = Hero('Daito', 6, 150, 15)
        with self.assertRaises(Exception) as ex:
            self.main_hero.battle(hero_self)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_health_is_zero_raises(self):
        self.main_hero.health = 0
        self.assertEqual(0, self.main_hero.health)
        with self.assertRaises(ValueError) as ex:
            self.main_hero.battle(self.hiro)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_health_is_less_than_zero_raises(self):
        self.main_hero.health = -5
        self.assertEqual(-5, self.main_hero.health)
        with self.assertRaises(ValueError) as ex:
            self.main_hero.battle(self.hiro)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_health_enemy_is_less_than_zero_raises(self):
        self.hiro.health = -5
        self.assertEqual(-5, self.hiro.health)
        self.assertEqual(100, self.main_hero.health)
        with self.assertRaises(ValueError) as ex:
            self.main_hero.battle(self.hiro)
        self.assertEqual(f"You cannot fight Hiro. He needs to rest", str(ex.exception))

    def test_fight_draw_case(self):
        self.hiro.health = 50
        result = self.main_hero.battle(self.hiro)
        self.assertEqual("Draw", result)

    def test_main_hero_winning(self):
        self.main_hero.damage = 200
        self.main_hero.health = 300
        result = self.main_hero.battle(self.hiro)
        self.assertEqual("You win", result)
        self.assertEqual(205, self.main_hero.damage)
        self.assertEqual(6, self.main_hero.level)
        self.assertEqual(105, self.main_hero.health)

    def test_enemy_winning(self):
        result = self.main_hero.battle(self.hiro)
        self.assertEqual("You lose", result)

        self.assertEqual(35, self.hiro.health)
        self.assertEqual(25, self.hiro.damage)
        self.assertEqual(11, self.hiro.level)

        self.assertTrue(self.main_hero.health < 0)

    def test_string_repr(self):
        self.assertEqual(f"Hero Daito: 5 lvl\nHealth: 100\nDamage: 10\n", str(self.main_hero))


if __name__ == '__main__':
    main()