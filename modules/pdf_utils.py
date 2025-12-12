
# """
# modules/pdf_utils.py

# Utility functions for handling PDF operations:

# - merge_pdfs: merge up to 6 PDFs into a single PDF, with optional /Title metadata.
# - split_pdf: split a PDF into two PDFs at a given page.

# Built using the 'pypdf' library (compatible with pypdf 4.x+, which no longer
# includes PdfMerger and instead uses PdfWriter for both read/write and merging).
# """

# from __future__ import annotations

# from pathlib import Path
# from typing import List, Tuple

# from pypdf import PdfReader, PdfWriter


# class PdfError(Exception):
#     """Custom exception for PDF-related errors."""
#     pass


# def merge_pdfs(
#     input_paths: List[str],
#     output_path: str,
#     title: str | None = None,
# ) -> None:
#     """
#     Merge multiple PDFs into a single output PDF using PdfWriter.

#     This implementation is compatible with pypdf 4.x+, where PdfMerger was
#     removed and PdfWriter is used for combining documents.

#     Args:
#         input_paths:
#             List of file paths to PDFs to merge (order is preserved).
#         output_path:
#             Output PDF path.
#         title:
#             Optional document title to set in PDF metadata (/Title).
#             This can influence the tab/window name in PDF viewers
#             such as Chrome or Edge.

#     Raises:
#         PdfError: if input files are missing or if an I/O / merge error occurs.
#     """
#     if not input_paths:
#         raise PdfError("No input PDFs provided.")

#     writer = PdfWriter()

#     try:
#         for p in input_paths:
#             pdf_path = Path(p)
#             if not pdf_path.is_file():
#                 raise PdfError(f"Input file not found: {pdf_path}")

#             # Read each input PDF
#             reader = PdfReader(str(pdf_path))

#             # Append all pages from this PDF into the combined writer
#             for page in reader.pages:
#                 writer.add_page(page)

#         # Set document metadata if a title is provided
#         if title:
#             writer.add_metadata({"/Title": title})

#         out_path = Path(output_path)
#         out_path.parent.mkdir(parents=True, exist_ok=True)

#         # Write the merged PDF to disk
#         with out_path.open("wb") as f_out:
#             writer.write(f_out)

#     except Exception as exc:  # noqa: BLE001
#         raise PdfError(f"Failed to merge PDFs: {exc}") from exc


# def split_pdf(
#     input_path: str,
#     split_page: int,
#     output_path_first: str,
#     output_path_second: str,
# ) -> Tuple[str, str]:
#     """
#     Split a PDF into two PDFs at the given split page.

#     Example:
#         If original PDF has 10 pages and split_page = 4:
#         - FIRST: pages 1-3
#         - SECOND: pages 4-10

#     Args:
#         input_path:
#             Path to the original PDF.
#         split_page:
#             Page number (1-based) at which to split.
#             This is the first page of the SECOND document.
#         output_path_first:
#             Output path for the first part (pages 1..split_page-1).
#         output_path_second:
#             Output path for the second part (pages split_page..end).

#     Returns:
#         Tuple of the output paths (first, second).

#     Raises:
#         PdfError: if pages are out of range, file does not exist,
#                   or on I/O / write issues.
#     """
#     src_path = Path(input_path)
#     if not src_path.is_file():
#         raise PdfError(f"Input PDF not found: {src_path}")

#     try:
#         reader = PdfReader(str(src_path))
#         total_pages = len(reader.pages)
#     except Exception as exc:  # noqa: BLE001
#         raise PdfError(f"Failed to read input PDF: {exc}") from exc

#     # Valid split range:
#     #   - split_page must be >= 2 (so the first document is non-empty)
#     #   - split_page must be <= total_pages (second doc gets at least one page)
#     if split_page <= 1 or split_page > total_pages:
#         raise PdfError(
#             f"Split page must be between 2 and {total_pages}, got {split_page}."
#         )

#     writer_first = PdfWriter()
#     writer_second = PdfWriter()

#     # FIRST PDF: pages 1..(split_page-1)
#     for i in range(0, split_page - 1):
#         writer_first.add_page(reader.pages[i])

#     # SECOND PDF: pages split_page..total_pages
#     for i in range(split_page - 1, total_pages):
#         writer_second.add_page(reader.pages[i])

#     out_first = Path(output_path_first)
#     out_second = Path(output_path_second)

#     out_first.parent.mkdir(parents=True, exist_ok=True)
#     out_second.parent.mkdir(parents=True, exist_ok=True)

#     try:
#         with out_first.open("wb") as f1:
#             writer_first.write(f1)
#         with out_second.open("wb") as f2:
#             writer_second.write(f2)
#     except Exception as exc:  # noqa: BLE001
#         raise PdfError(f"Failed to write split PDFs: {exc}") from exc

#     return str(out_first), str(out_second)













"""
modules/pdf_utils.py

Utility functions for handling PDF operations:

- merge_pdfs: merge up to 6 PDFs into a single PDF, with optional /Title metadata.
- split_pdf: split a PDF into two PDFs at a given page, with optional titles for
             each resulting document.

Built using the 'pypdf' library (compatible with pypdf 4.x+, which no longer
includes PdfMerger and instead uses PdfWriter for both read/write and merging).
"""

from __future__ import annotations

from pathlib import Path
from typing import List, Tuple

from pypdf import PdfReader, PdfWriter


class PdfError(Exception):
    """Custom exception for PDF-related errors."""
    pass


def merge_pdfs(
    input_paths: List[str],
    output_path: str,
    title: str | None = None,
) -> None:
    """
    Merge multiple PDFs into a single output PDF using PdfWriter.

    Args:
        input_paths:
            List of file paths to PDFs to merge (order is preserved).
        output_path:
            Output PDF path.
        title:
            Optional document title to set in PDF metadata (/Title).
            This can influence the tab/window name in PDF viewers
            such as Chrome or Edge.

    Raises:
        PdfError: if input files are missing or if an I/O / merge error occurs.
    """
    if not input_paths:
        raise PdfError("No input PDFs provided.")

    writer = PdfWriter()

    try:
        for p in input_paths:
            pdf_path = Path(p)
            if not pdf_path.is_file():
                raise PdfError(f"Input file not found: {pdf_path}")

            # Read each input PDF
            reader = PdfReader(str(pdf_path))

            # Append all pages from this PDF into the combined writer
            for page in reader.pages:
                writer.add_page(page)

        # Set document metadata if a title is provided
        if title:
            writer.add_metadata({"/Title": title})

        out_path = Path(output_path)
        out_path.parent.mkdir(parents=True, exist_ok=True)

        # Write the merged PDF to disk
        with out_path.open("wb") as f_out:
            writer.write(f_out)

    except Exception as exc:  # noqa: BLE001
        raise PdfError(f"Failed to merge PDFs: {exc}") from exc


def split_pdf(
    input_path: str,
    split_page: int,
    output_path_first: str,
    output_path_second: str,
    first_title: str | None = None,
    second_title: str | None = None,
) -> Tuple[str, str]:
    """
    Split a PDF into two PDFs at the given split page.

    Example:
        If original PDF has 10 pages and split_page = 4:
        - FIRST: pages 1-3
        - SECOND: pages 4-10

    Args:
        input_path:
            Path to the original PDF.
        split_page:
            Page number (1-based) at which to split.
            This is the first page of the SECOND document.
        output_path_first:
            Output path for the first part (pages 1..split_page-1).
        output_path_second:
            Output path for the second part (pages split_page..end).
        first_title:
            Optional /Title metadata for the FIRST PDF (browser tab name).
            If None, the FIRST PDF inherits the original PDF's title (if any).
        second_title:
            Optional /Title metadata for the SECOND PDF (browser tab name).
            If None, the SECOND PDF inherits the original PDF's title (if any).

    Returns:
        Tuple of the output paths (first, second).

    Raises:
        PdfError: if pages are out of range, file does not exist,
                  or on I/O / write issues.
    """
    src_path = Path(input_path)
    if not src_path.is_file():
        raise PdfError(f"Input PDF not found: {src_path}")

    try:
        reader = PdfReader(str(src_path))
        total_pages = len(reader.pages)
        original_title = None
        if reader.metadata and "/Title" in reader.metadata:
            original_title = str(reader.metadata["/Title"])
    except Exception as exc:  # noqa: BLE001
        raise PdfError(f"Failed to read input PDF: {exc}") from exc

    # Valid split range:
    #   - split_page must be >= 2 (so the first document is non-empty)
    #   - split_page must be <= total_pages (second doc gets at least one page)
    if split_page <= 1 or split_page > total_pages:
        raise PdfError(
            f"Split page must be between 2 and {total_pages}, got {split_page}."
        )

    writer_first = PdfWriter()
    writer_second = PdfWriter()

    # FIRST PDF: pages 1..(split_page-1)
    for i in range(0, split_page - 1):
        writer_first.add_page(reader.pages[i])

    # SECOND PDF: pages split_page..total_pages
    for i in range(split_page - 1, total_pages):
        writer_second.add_page(reader.pages[i])

    # Metadata for each output:
    # If explicit title given, use that; otherwise inherit original title (if any).
    effective_first_title = first_title or original_title
    effective_second_title = second_title or original_title

    if effective_first_title:
        writer_first.add_metadata({"/Title": effective_first_title})
    if effective_second_title:
        writer_second.add_metadata({"/Title": effective_second_title})

    out_first = Path(output_path_first)
    out_second = Path(output_path_second)

    out_first.parent.mkdir(parents=True, exist_ok=True)
    out_second.parent.mkdir(parents=True, exist_ok=True)

    try:
        with out_first.open("wb") as f1:
            writer_first.write(f1)
        with out_second.open("wb") as f2:
            writer_second.write(f2)
    except Exception as exc:  # noqa: BLE001
        raise PdfError(f"Failed to write split PDFs: {exc}") from exc

    return str(out_first), str(out_second)
