%global tl_name marginfit
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Improved margin notes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/marginfit
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/marginfit.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/marginfit.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/marginfit.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package fixes various bugs with the margin paragraph implementation
of LaTeX. Those bugs include margin notes that are attached to the wrong
side as well as those that stick out of the bottom of the page. This
package provides a drop-in replacement solution.

