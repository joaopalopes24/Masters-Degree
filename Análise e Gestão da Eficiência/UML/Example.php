<?php

namespace App;

use App\Actions\Abstract;
use App\Actions\Contract;
use Illuminate\Support\Carbon;

class Example
{
    /**
     * Test using Abstract.
     */
    public function test1(): void
    {
        $checkin = Carbon::createFromFormat('Y-m-d', '2025-01-01');
        $checkout = Carbon::createFromFormat('Y-m-d', '2025-01-05');

        $reservation = new Reservation(649.99, $checkin, $checkout);

        $reservation->save();

        Abstract\ConfirmReservation::execute($reservation);

        dump($reservation->getStatus());

        Abstract\CancelReservation::execute($reservation);

        dump($reservation->getStatus());

        $check = Abstract\CheckIfReservationWasFinished::execute($reservation);

        dd($check);
    }

    /**
     * Test using Contract.
     */
    public function test2(): void
    {
        $checkin = Carbon::createFromFormat('Y-m-d', '2025-01-01');
        $checkout = Carbon::createFromFormat('Y-m-d', '2025-01-05');

        $reservation = new Reservation(649.99, $checkin, $checkout);

        $reservation->save();

        (new Contract\ConfirmReservation($reservation))->handle();

        dump($reservation->getStatus());

        (new Contract\CancelReservation($reservation))->handle();

        dump($reservation->getStatus());

        $check = (new Contract\CheckIfReservationWasFinished($reservation))->handle();

        dd($check);
    }
}
