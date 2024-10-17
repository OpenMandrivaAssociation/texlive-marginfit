Name:		texlive-marginfit
Version:	48281
Release:	2
Summary:	Improved margin notes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/marginfit
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/marginfit.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/marginfit.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/marginfit.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package fixes various bugs with the margin paragraph
implementation of LaTeX. Those bugs include margin notes that
are attached to the wrong side as well as those that stick out
of the bottom of the page. This package provides a drop-in
replacement solution.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/marginfit
%{_texmfdistdir}/tex/latex/marginfit
%doc %{_texmfdistdir}/doc/latex/marginfit

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
