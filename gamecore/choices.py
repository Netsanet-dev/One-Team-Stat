from django.db import models


class PlayerPositions(models.TextChoices):
    GK = 'GK', 'GoalKeeper',
    FB = 'FB', 'Full Back'
    CB = 'CB', 'Central Defender',
    LB = 'LB', 'Left Back',
    RB = 'RB', 'Right Back',
    WB = 'WB', 'Wing Back',
    DM = 'DM', 'Defensive Midfielder',
    CM = 'CM', 'Central Midfielder',
    AM = 'AM', 'Attacking Midfielder',
    WM = 'WM', 'Winger',
    ST = 'ST', 'Striker',
    WF = 'WF', 'Winger Forward',

class DominantFoot(models.TextChoices):
    RIGHT = 'right', 'Right',
    LEFT = 'left', 'Left',

class Gender(models.TextChoices):
    MALE = 'M', 'Male',
    FEMALE = 'F', 'Female',

class TeamDivisons(models.TextChoices):
    FIRST = 'first', 'First Team',
    SECOND = 'second', 'second',
    U21 = 'U21', 'Under 21',
    U18 = 'U18', 'Under 18',
    U16 = 'U16', 'Under 16',
    OTHER = 'Other', 'Other',

class LeagueDivisions(models.TextChoices):
    TOP = 'Top', 'Professional League',
    SECOND = 'second', 'Second League',
    THIRD = 'Third', 'Third League',
    AMATEUR = 'Amateur', 'Amaterur League'

class CoachingPositions(models.TextChoices):
    MANAGER = 'Manager', 'Manager',
    ACADAMY = 'Acadamy', 'Acadamy Director',
    HEAD = 'head', 'Head Coach',
    ASSISTANT = 'assistant', 'Assistant Coach',
    FIRST_TEAM = 'First team', 'First team Coach',
    GOALKEEPING= 'Goalkeeping', 'Goalkeeping Coach',
    FITNESS = 'Fitness', 'Fitness Coach',
    TACTICAL = 'Tactical', 'Tactical Coach',
    PERFORMANCE = 'Performace', 'Performace Analyst',
    YOUTH = 'Youth', 'Youth Coach',
    SET_PIECE = 'set-piece', 'Set-Piece Coach',
    REHABILITAION = 'Rehabilitaion', 'Rehabilitaion Coach',
    SCOUT = 'Scout', 'Scout',


class RefereeLevel(models.TextChoices):
    FIFA = 'fifa', 'Fifa'
    NATIONAL = 'national', 'National'
    REGIONAL = 'regional', 'Regional'
    Local = 'local', 'Local'
    OTHER = 'other', 'Other'