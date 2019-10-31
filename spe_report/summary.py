from typing import List, Dict
import os
from smtplib import SMTP, SMTPException
from email.mime.text import MIMEText
from autologging import logged, traced
from datetime import datetime

from spe_utils.constants import SMPT_DEBUG, SMPT_FROM, SMPT_TO, SMPT_HOST, SMPT_PORT, PLACEMENT, VALIDATION


@traced
@logged
class SPESummaryReport:
    def __init__(self):
        self.stored_persisted_date: Dict[str, str] = dict()
        self.ext_stored_persisted_date: Dict[str, str] = dict()
        self.used_query_date: Dict[str, str] = dict()

        self.start_time: str = None
        self.end_time: str = None
        self.elapsed_time: str = None

        self.full_score_list: Dict[str, List[Dict[str, str]]] = {PLACEMENT: [], VALIDATION: []}
        self.sent_score_list: Dict[str, List[Dict[str, str]]] = {PLACEMENT: [], VALIDATION: []}
        self.not_sent_scores_list: Dict[str, List[Dict[str, str]]] = {PLACEMENT: [], VALIDATION: []}
        self.course_id: Dict[str, str] = dict()

    def get_subject(self):
        sub_test: str = f'Spanish Placement Exam Processing Summary {datetime.now().replace(microsecond=0)}'
        return f"P({len(self.sent_score_list[PLACEMENT])}/{len(self.full_score_list[PLACEMENT])}):V({len(self.sent_score_list[VALIDATION])}/{len(self.full_score_list[VALIDATION])}) {sub_test}"

    def email_report(self):
        msg = f"""
        Summary of Spanish Placement Exam processing.  
        This report includes the report runtimes, the cutoff times used for querying for new users, and counts of users added and errors.
        The subject line of the corresponding email summarizes the scores added/received as (n/n) for Placement/Validation tests.
        
        starting time: {self.start_time}
        end time: {self.end_time}
        elapsed time: {self.elapsed_time}

        storedTestLastTakenTime: {self.stored_persisted_date}
        useTestLastTakenTime: {self.used_query_date}
        updatedTestLastTakenTime: {self.next_stored_persisted_date}
        
        
        course_id: {self.course_id}
        
         """
        return msg

    def email_msg(self):
        msg: List[str] = list()
        msg.append(self.email_report())
        msg.append(f"Placement user scores added: {len(self.sent_score_list[PLACEMENT])} failed: {len(self.not_sent_scores_list[PLACEMENT])}")
        if self.sent_score_list[PLACEMENT]:
            msg.append("Placement Success users List:")
            for item in self.sent_score_list[PLACEMENT]:
                msg.append(f"user: {item['user']}  score: {item['score']}  finished_at: {item['local_submitted_date']}")
            msg.append("\n")
        if self.not_sent_scores_list[PLACEMENT]:
            msg.append("Failed sending Placement scores below, will try in the next run")
            for item in self.not_sent_scores_list[PLACEMENT]:
                msg.append(f"user: {item['user']}  score: {item['score']}  finished_at: {item['local_submitted_date']}")
            msg.append("\n")

        msg.append(f"Validation user scores added: {len(self.sent_score_list[VALIDATION])} failed: {len(self.not_sent_scores_list[VALIDATION])}")
        if self.sent_score_list[VALIDATION]:
            msg.append("Validation Success users List:")
            for item in self.sent_score_list[VALIDATION]:
                msg.append(f"user: {item['user']}  score: {item['score']}  finished_at: {item['local_submitted_date']}")
            msg.append("\n")
        if self.not_sent_scores_list[VALIDATION]:
            msg.append("Failed sending Validation scores below, will try in the next run")
            for item in self.not_sent_scores_list[VALIDATION]:
                msg.append(f"user: {item['user']}  score: {item['score']}  finished_at: {item['local_submitted_date']}")
            msg.append("\n")

        return msg

    def is_any_scores_received(self):
        if self.full_score_list[PLACEMENT] or self.full_score_list[VALIDATION]:
            return True
        return False

    def send_email(self):
        port: str = os.getenv(SMPT_PORT)
        host: str = os.getenv(SMPT_HOST)
        to_address: str = os.getenv(SMPT_TO)
        from_address: str = os.getenv(SMPT_FROM)
        email_debug: int = int(os.getenv(SMPT_DEBUG)) if os.getenv(SMPT_DEBUG) else 0
        try:
            smtpObj: SMTP = SMTP(host, port)
            smtpObj.set_debuglevel(email_debug)
            msg = MIMEText('\n'.join(self.email_msg()))
            msg['Subject'] = self.get_subject()
            msg['From'] = from_address
            msg['To'] = to_address
            smtpObj.send_message(msg)
            self.__log.info("Successfully sent email")
        except SMTPException as e:
            self.__log.info(f"Error: unable to send email due to {e}")

