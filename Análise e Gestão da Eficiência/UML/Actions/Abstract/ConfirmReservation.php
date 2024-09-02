<?php

namespace App\Actions\Abstract;

use App\Abstracts\Action;
use App\Enums\StatusEnum;
use App\Reservation;

class ConfirmReservation extends Action
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
    protected function handle(): void
    {
        $this->reservation->setStatus(StatusEnum::CONFIRMED);

        $this->reservation->save();
    }
}
