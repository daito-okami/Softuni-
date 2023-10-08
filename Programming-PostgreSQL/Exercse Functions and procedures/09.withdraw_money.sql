CREATE OR REPLACE PROCEDURE sp_withdraw_money(
    account_id INT,
    money_amount NUMERIC(10, 4)
)AS
$$
    DECLARE
        current_balance numeric;
    begin
        current_balance := (SELECT balance from accounts where id = account_id);

        if (current_balance - money_amount) >= 0 THEN
            update accounts
            SET balance = balance- money_amount
            WHERE id = account_id;
        ELSE
            RAISE NOTICE 'Insufficient balance to withdraw %', money_amount;
        end if;
    end;
$$
LANGUAGE plpgsql

