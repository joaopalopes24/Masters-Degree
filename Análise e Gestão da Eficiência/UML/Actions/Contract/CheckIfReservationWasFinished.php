<?php

namespace App\Actions\Contract;

use App\Contracts\Execute;
use App\Enums\StatusEnum;
use App\Reservation;

class CheckIfReservationWasFinished implements Execute
{
    /**
     * Create a new Reservation instance.
     */
    public function __construct(
        private Reservation $reservation,
    ) {}

    /**
     * Execute the action.
     */
    public function handle(): bool
    {
        if ($this->reservation->getStatus() !== StatusEnum::CONFIRMED) {
            return false;
        }

        $checkout = $this->reservation->getCheckout();

        return $checkout->isPast();
    }
}
