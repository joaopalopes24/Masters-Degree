<?php

namespace App\Enums;

enum StatusEnum: int
{
    case PENDING = 1;
    case CONFIRMED = 2;
    case CANCELED = 3;
}
