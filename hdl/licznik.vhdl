--------------------------------------------------------------------------------
-- SubModule licz8
-- Created 30.03.2016 11:53:26
-- Licznik binarny rewersyjny - LAB 3, SPR 2
--------------------------------------------------------------------------------
LIBRARY IEEE;
USE IEEE.Std_Logic_1164.ALL;
USE IEEE.numeric_std.ALL;

ENTITY licznik IS PORT (
    clk : IN STD_LOGIC;
    reset : IN STD_LOGIC;
    DIR : IN STD_LOGIC;
    led : OUT STD_LOGIC_VECTOR(3 DOWNTO 0)
);
END licznik;
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
ARCHITECTURE Structure OF licznik IS
    SIGNAL q : STD_LOGIC_VECTOR(3 DOWNTO 0) := (OTHERS => '0');
BEGIN

    PROCESS (clk, reset)
    BEGIN
        IF reset = '1' THEN
            q <= "0000";
        ELSIF (clk'event AND clk = '1') THEN
            IF DIR = '1' THEN
                q <= STD_LOGIC_VECTOR(unsigned(q) + 1);
            ELSE
                q <= STD_LOGIC_VECTOR(unsigned(q) - 1);
            END IF;
        END IF;
    END PROCESS;
    led <= q;

END Structure;
--------------------------------------------------------------------------------