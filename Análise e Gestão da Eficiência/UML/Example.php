<?php

namespace App;

use App\Actions\CancelReservation;
use App\Actions\CheckIfReservationWasFinished;
use App\Actions\ConfirmReservation;
use Illuminate\Support\Carbon;

class Example
{
    public function __invoke(): void
    {
        $checkin = Carbon::createFromFormat('Y-m-d', '2025-01-01');
        $checkout = Carbon::createFromFormat('Y-m-d', '2025-01-05');

        $reservation = new Reservation(649.99, $checkin, $checkout);

        $reservation->save();

        (new ConfirmReservation($reservation))->handle();

        dump($reservation->getStatus());

        (new CancelReservation($reservation))->handle();

        dump($reservation->getStatus());

        $check = (new CheckIfReservationWasFinished($reservation))->handle();

        dd($check);
    }
}
