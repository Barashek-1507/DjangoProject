          function Out(){
            var rad1 = document.getElementsByName("state");
            var rad2 = document.getElementsByName("state1");
            var rad3 = document.getElementsByName("state2");
            var rad4 = document.getElementsByName("state3");
            var rad5 = document.getElementsByName("state4");

            points = 0;

            for (var i = 0; i < rad1.length; i++) {
                if (rad1[i].checked & rad1[i] == rad1[0]) {
                    points += 1;
                }
            }
            for (var i = 0; i < rad2.length; i++) {
                if (rad2[i].checked & rad2[i] == rad2[2]) {
                    points += 1;
                }
            }
            for (var i = 0; i < rad3.length; i++) {
                if (rad3[i].checked & rad3[i] == rad3[1]) {
                    points += 1;
                }
            }
            for (var i = 0; i < rad4.length; i++) {
                if (rad4[i].checked & rad4[i] == rad4[0]) {
                    points += 1;
                }
            }
            for (var i = 0; i < rad5.length; i++) {
                if (rad5[i].checked & rad5[i] == rad5[1]) {
                    points += 1;
                }
            }

            var result = points / 5 * 100;
            document.getElementById("res").innerHTML = "Результаты теста в процентах: " + result + "%";
            console.log(result);

            if ((result == 100)) {
                document.getElementById("recommendation").value = "Результаты промежуточно тестирования показали высокий уровень знаний и ваш опыт работы нам подходит, приглашаем на второй уровень собседования. ";
            } else if ((result <= 100) && (result >= 75) && (ex >= 10)) {
                document.getElementById("recommendation").value = "По результатам тестирования мы можем сделать выводы, что вы хорошо владеете информацией, приглашаем на следующий уровень собеседования. ";
            } else if ((result <= 100) && (result >= 75) && (ex < 10)) {
                document.getElementById("recommendation").value = " Уровень ваших знаний нас порадовал, но, к сожалению, вам не хватает опыта работы. Можем вам порекомендовать пройти стажировку на должность пониже.";
            } else if (result < 50) {
                document.getElementById("recommendation").value = "К сожалению, ваш уровень знаний на данном этапе нас не устраивает. Рекомендуем вам повысить уровень ваших знаний.";            }
            }
//            document.getElementById("").innerHTML = "Результаты теста в процентах: " + result + "%";
//
//            if ((result == 100)) {
//                document.getElementById("res10").innerHTML = " Общие рекомендации: Результаты промежуточно тестирования показали высокий уровень знаний и ваш опыт работы нам подходит, приглашаем на второй уровень собседования. ";
//                localStorage.setItem('recomend', 'Результаты промежуточно тестирования показали высокий уровень знаний и ваш опыт работы нам подходит, приглашаем на второй уровень собседования.');
//            } else if ((result <= 100) && (result >= 75) && (ex >= 10)) {
//                document.getElementById("res10").innerHTML = " Общие рекомендации: По результатам тестирования мы можем сделать выводы, что вы хорошо владеете информацией, приглашаем на следующий уровень собеседования. ";
//                localStorage.setItem('recomend', 'По результатам тестирования мы можем сделать выводы, что вы хорошо владеете информацией, приглашаем на следующий уровень собеседования.');
//            } else if ((result <= 100) && (result >= 75) && (ex < 10)) {
//                document.getElementById("res10").innerHTML = " Общие рекомендации: Уровень ваших знаний нас порадовал, но, к сожалению, вам не хватает опыта работы. Можем вам порекомендовать пройти стажировку на должность пониже.";
//                localStorage.setItem('recomend', 'Уровень ваших знаний нас порадовал, но, к сожалению, вам не хватает опыта работы. Можем вам порекомендовать пройти стажировку на должность пониже.');
//
//            } else if (result < 75) {
//                document.getElementById("res10").innerHTML = " Общие рекомендации: К сожалению, ваш уровень знаний на данном этапе нас не устраивает. Рекомендуем вам повысить уровень ваших знаний.";
//                localStorage.setItem('recomend', 'К сожалению, ваш уровень знаний на данном этапе нас не устраивает. Рекомендуем вам повысить уровень ваших знаний.');
//            }