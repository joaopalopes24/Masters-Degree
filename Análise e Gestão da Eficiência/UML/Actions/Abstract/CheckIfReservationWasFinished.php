<?php

namespace App\Actions\Abstract;

use App\Abstracts\Action;
use App\Enums\StatusEnum;
use App\Reservation;

class CheckIfReservationWasFinished extends Action
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
    protected function handle(): bool
    {
        if ($this->reservation->getStatus() !== StatusEnum::CONFIRMED) {
            return false;
        }

        $checkout = $this->reservation->getCheckout();

        return $checkout->isPast();
    }
}
